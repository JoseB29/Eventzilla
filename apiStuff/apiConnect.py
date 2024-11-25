import os
import requests

class TicketmasterAPI:
    def __init__(self, api_url, image_folder):
        self.api_url = api_url
        self.events = []
        self.image_folder = image_folder
        self.image_paths = {}  # Dictionary to store image paths for events

    def fetch_events(self):
        """
        Fetch events from the Ticketmaster API and store them in the events attribute.
        """
        response = requests.get(self.api_url)

        if response.status_code == 200:
            data = response.json()
            self.events = data.get('_embedded', {}).get('events', [])
            print(f"Total Events Found: {len(self.events)}")
            self.clear_image_folder()  # Clear the image folder before saving new images
            self.save_images()  # Save the images for each event
        else:
            print(f"API call failed with status code {response.status_code}")
            self.events = []

    def get_events(self):
        """
        Return the list of events stored in the API class.
        """
        return self.events

    def clear_image_folder(self):
        """
        Delete all images in the folder before adding new ones.
        """
        for filename in os.listdir(self.image_folder):
            file_path = os.path.join(self.image_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted {filename} from the image folder.")

    def save_images(self):
        """
        Save the second image of each event in the specified folder and store the file paths in the dictionary.
        """
        for event in self.events:
            images = event.get('images', [])
            if len(images) > 1:  # Check if a second image exists
                image_url = images[1].get('url')
                image_name = f"{event.get('id')}_image.jpg"  # Use event ID as image name
                image_path = os.path.join(self.image_folder, image_name)

                # Download and save the image
                try:
                    image_response = requests.get(image_url)
                    if image_response.status_code == 200:
                        with open(image_path, 'wb') as file:
                            file.write(image_response.content)
                        self.image_paths[event.get('id')] = image_path  # Store the image path
                        print(f"Saved image for event {event.get('id')} to {image_path}")
                    else:
                        print(f"Failed to download image for event {event.get('id')}")
                except Exception as e:
                    print(f"Error downloading image for event {event.get('id')}: {e}")

class TicketmasterPrinter:
    def __init__(self, events, image_paths):
        self.events = events
        self.image_paths = image_paths  # Dictionary of image paths

    def print_event_details(self, event):
        """
        Print the details of a single event, including the image path.
        """
        # Extract event details
        name = event.get('name', 'N/A')
        event_type = event.get('type', 'N/A')
        event_id = event.get('id', 'N/A')
        event_url = event.get('url', 'N/A')
        locale = event.get('locale', 'N/A')

        # Print general event info
        print(f"Event Information")
        print(f"Name: {name}")
        print(f"Type: {event_type}")
        print(f"Event ID: {event_id}")
        print(f"URL: {event_url}")
        print(f"Locale: {locale}")

        # Extract and print image info (second image if available)
        images = event.get('images', [])
        if len(images) > 1:  # Check if there is a second image
            second_image_url = images[1].get('url', 'No second image available')
            print(f"Second Image URL: {second_image_url}")
            # Print the saved image path
            saved_image_path = self.image_paths.get(event_id, 'Image path not available')
            print(f"Saved Image Path: {saved_image_path}")
        else:
            print(f"Second Image URL: Not Available")

        # Extract sales details
        sales = event.get('sales', {})
        public_sales = sales.get('public', {})
        public_start = public_sales.get('startDateTime', 'N/A')
        public_end = public_sales.get('endDateTime', 'N/A')

        print("\nSales Details")
        print(f"Public Sales:")
        print(f"Start Date: {public_start}")
        print(f"End Date: {public_end}")

        # Extract event date and time
        dates = event.get('dates', {})
        local_date = dates.get('start', {}).get('localDate', 'N/A')
        local_time = dates.get('start', {}).get('localTime', 'N/A')
        utc_date = dates.get('start', {}).get('utcDate', 'N/A')
        utc_time = dates.get('start', {}).get('utcTime', 'N/A')

        print("\nEvent Date & Time")
        print(f"Local Date/Time: {local_date} {local_time}")
        print(f"UTC Date/Time: {utc_date} {utc_time}")

        # Classifications
        classifications = event.get('classifications', [{}])
        category = classifications[0].get('segment', {}).get('name', 'N/A')
        genre = classifications[0].get('genre', {}).get('name', 'N/A')
        subgenre = classifications[0].get('subGenre', {}).get('name', 'N/A')

        print("\nClassifications")
        print(f"Category: {category}")
        print(f"Genre: {genre}")
        print(f"Subgenre: {subgenre}")

        # Venue details
        venue = event.get('_embedded', {}).get('venues', [{}])[0]
        venue_name = venue.get('name', 'N/A')
        venue_address = venue.get('address', {}).get('line1', 'N/A')
        venue_city = venue.get('city', {}).get('name', 'N/A')
        venue_state = venue.get('state', {}).get('stateCode', 'N/A')
        venue_country = venue.get('country', {}).get('countryCode', 'N/A')

        print("\nVenue Details")
        print(f"Venue Name: {venue_name}")
        print(f"Address: {venue_address}")
        print(f"City/State: {venue_city}, {venue_state}")
        print(f"Country: {venue_country}")

        # Promoter details
        promoters = event.get('promoters', [])
        if promoters:
            primary_promoter = promoters[0].get('name', 'N/A')
            additional_promoter = promoters[1].get('name', 'N/A') if len(promoters) > 1 else 'N/A'
            print("\nPromoters")
            print(f"Primary Promoter: {primary_promoter}")
            print(f"Additional Promoter: {additional_promoter}")
        else:
            print("\nPromoters: Not Available")

        # Ticket details
        price_range = event.get('priceRanges', [{}])
        min_price = price_range[0].get('min', 'N/A')
        max_price = price_range[0].get('max', 'N/A')

        print("\nTicket Details")
        print(f"Price Range: {min_price} - {max_price}")

        # Accessibility information
        accessibility = event.get('accessibility', {})
        accessible_seating = accessibility.get('seating', 'N/A')
        print("\nAccessibility")
        print(f"Accessible Seating: {accessible_seating}")

    def print_all_event_details(self):
        """
        Print details for all events stored in the events attribute.
        """
        if self.events:
            print(f"\nTotal Events Found: {len(self.events)}\n")
            for i, event in enumerate(self.events, start=1):
                print(f"\n\n--- Event {i} ---\n")
                self.print_event_details(event)
        else:
            print("No events available.")


# Main Execution
if __name__ == "__main__":
    apiCall = "https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&dmaId=324&apikey=9QIWlk2dq8iktJZ8FtiX9vGSmNyhN2gW"
    image_folder = "event_images"  # Directory to save images
    
    # Create the image folder if it doesn't exist
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    # Create an instance of the TicketmasterAPI class and fetch events
    ticketmaster_api = TicketmasterAPI(apiCall, image_folder)
    ticketmaster_api.fetch_events()

    # Create an instance of the TicketmasterPrinter class
    ticketmaster_printer = TicketmasterPrinter(
        ticketmaster_api.get_events(),  # List of events
        ticketmaster_api.image_paths   # Dictionary of image paths
    )

    # Print all event details
    ticketmaster_printer.print_all_event_details()
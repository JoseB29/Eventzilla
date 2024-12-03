import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import json

class EventPageInfoTwo(tk.Frame):
    def __init__(self, master, event_info):
        super().__init__(master)
        self.master = master
        self.current_page = None
        self.event_info = event_info
        self.create_widgets()


    def create_widgets(self):
        self.configure(bg="#F5F5F5")  # Set background for the entire page
        self.master.title("Event Details")
        self.master.geometry("390x934")  # iPhone size

        # Styling
        self.bg_color = "#F5F5F5"
        self.btn_color = "#D3D3D3"  # Light gray for button

        total_height = 844
        top_bar_height = 90
        bottom_bar_height = 90

        # Green bar at the top
        self.green_bar = tk.Frame(self, bg="#25A03D", height=top_bar_height)
        self.green_bar.pack(fill="x", side="top")
        self.green_bar.pack_propagate(False)
        
   

        # Add the arrow image to the top-left corner
        arrow_image = Image.open("appElements\\arrowFacingLeft.png")
        arrow_resized = arrow_image.resize((45, 45), Image.LANCZOS)  # Resize image if necessary
        arrow_photo = ImageTk.PhotoImage(arrow_resized)

        self.arrow_label = tk.Label(self.green_bar, image=arrow_photo, bg="#25A03D", cursor="hand2")  # Change cursor to a pointer
        self.arrow_label.image = arrow_photo  # Keep a reference to avoid garbage collection
        self.arrow_label.place(x=15, y=22)  # Position in the top-left corner with some padding

        # Bind click event to the arrow image
        self.arrow_label.bind("<Button-1>", self.arrow_clicked)

        # Title in the green bar
        self.title = tk.Label(self.green_bar, text="Event Details", font=("Helvetica", 24, "bold"), fg="white", bg="#25A03D")
        self.title.pack(expand=True)

        #now display the event info
        event_name = self.event_info["name"]
        event_date = self.event_info["local_date"]
        event_time = self.event_info["local_time"]
        event_venue = self.event_info["venue_name"]
        event_city = self.event_info["venue_city"]
        event_state = self.event_info["venue_state"]
        event_image = self.event_info["image_path"]
        event_url = self.event_info["event_url"]

        # Display the event picture right below the top green bar
        event_image = Image.open(event_image)
        resized_event_image = event_image.resize((390, 300), Image.LANCZOS)
        event_photo = ImageTk.PhotoImage(resized_event_image)

        # Create label to display the image
        self.event_image_label = tk.Label(self, image=event_photo)
        self.event_image_label.image = event_photo  # Keep a reference to avoid garbage collection
        self.event_image_label.pack(pady=10)

        # Display event details
        details_frame = tk.Frame(self, bg=self.bg_color)
        details_frame.pack(pady=10, padx=10, fill="both")

        title_text = f"Event: {event_name}"

        # Adjust the font size for long event names
        font_size = 16 if len(event_name) <= 25 else 14  # Reduce font size for longer names

        event_name_label = tk.Label(
            details_frame, 
            text=title_text, 
            font=("Helvetica", font_size, "bold"), 
            bg=self.bg_color, 
            wraplength=350,  # Optional: wrap the text if needed
            justify="left"
        )
        event_name_label.pack(anchor="w", pady=5)

        event_date_label = tk.Label(details_frame, text=f"Date: {event_date}", font=("Helvetica", 12), bg=self.bg_color)
        event_date_label.pack(anchor="w", pady=5)

        event_time_label = tk.Label(details_frame, text=f"Time: {event_time}", font=("Helvetica", 12), bg=self.bg_color)
        event_time_label.pack(anchor="w", pady=5)

        event_venue_label = tk.Label(details_frame, text=f"Venue: {event_venue}", font=("Helvetica", 12), bg=self.bg_color)
        event_venue_label.pack(anchor="w", pady=5)

        event_location_label = tk.Label(details_frame, text=f"Location: {event_city}, {event_state}", font=("Helvetica", 12), bg=self.bg_color)
        event_location_label.pack(anchor="w", pady=5)

        # Now add the buy ticket button under the location label
        buy_ticket_image = Image.open("appElements/buyTicketButton.png")
        resized_buy_ticket_image = buy_ticket_image.resize((200, 50), Image.LANCZOS)
        buy_ticket_photo = ImageTk.PhotoImage(resized_buy_ticket_image)

        # Create a button and use the event_url to open the URL in the default browser
        buy_ticket_button = tk.Button(details_frame, 
                                      image=buy_ticket_photo, 
                                      command=lambda: webbrowser.open(event_url),  # Open the event URL
                                      bg=self.bg_color, 
                                      bd=0)
        buy_ticket_button.image = buy_ticket_photo  # Keep a reference to avoid garbage collection
        buy_ticket_button.pack(pady=10)

        #add to favorites button
        def prinmt():
            print("Favorite button clicked")
            email = self.master.email

            try:
                # Open the JSON file and load the data
                with open("myEvents.json", "r") as file:
                    data = json.load(file)
                    # Ensure data is a list
                    if not isinstance(data, list):
                        raise ValueError("JSON data is not a list")
            except (FileNotFoundError, json.JSONDecodeError, ValueError):
                # If the file does not exist, is empty, or has invalid JSON, initialize `data` as an empty list
                data = []

            # Find the user object by email
            user = next((item for item in data if item.get("email") == email), None)

            if user is None:
                # If the user does not exist, create a new entry with the event info
                data.append({"email": email, "favorites": [self.event_info]})
            else:
                # If the user exists, ensure `favorites` exists and add the event if not already present
                if "favorites" not in user:
                    user["favorites"] = []
                if self.event_info not in user["favorites"]:
                    user["favorites"].append(self.event_info)

            # Write the updated data back to the JSON file
            with open("myEvents.json", "w") as file:
                json.dump(data, file, indent=4)
            
            #add event_image to the saved events pics folder
            event_image.save(f"saved_events_pics/{self.event_info['name']}.png")
        

            print("Event added to favorites!")



        #Now add the favorite button under the buy ticket button
        favorite_image = Image.open("appElements/favButton.png")
        resized_favorite_image = favorite_image.resize((50, 50), Image.LANCZOS)
        favorite_photo = ImageTk.PhotoImage(resized_favorite_image)

        # Create a button and print a message when clicked
        favorite_button = tk.Button(details_frame, 
                                    image=favorite_photo, 
                                    command=prinmt,  # Print a message
                                    bg=self.bg_color, 
                                    bd=0)
        favorite_button.image = favorite_photo
        favorite_button.pack(pady=10)
        
        #add text under the favorite button
        favorite_text = tk.Label(details_frame, text="Favorite Event", font=("Helvetica", 12), bg=self.bg_color)
        favorite_text.pack(pady=10)

        # Bottom Bar
        self.bottom_bar = tk.Frame(self, bg="#25A03D", height=bottom_bar_height)
        self.bottom_bar.pack(side="bottom", fill="x")
        self.bottom_bar.pack_propagate(False)

        self.create_bottom_bar()

    def arrow_clicked(self, event):
        print("Arrow clicked!")
        self.master.switch_to_for_you_page()


    def create_bottom_bar(self):
        self.bottom_bar.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.add_bottom_bar_item("appElements\\magnifyingIconMagnifying.webp", "Search", 0, self.search_clicked)
        self.add_bottom_bar_item("appElements\\for_you_logo.png", "For You", 1, self.for_you_clicked)
        self.add_bottom_bar_item("appElements\\ticketLogo.png", "My Events", 2, self.my_events_clicked)
        self.add_bottom_bar_item("appElements\\profile_icon.webp", "Profile", 3, self.profile_clicked)

    def add_bottom_bar_item(self, image_path, label_text, column, click_function):
        icon = Image.open(image_path)
        resized_icon = icon.resize((50, 50), Image.LANCZOS)
        photo = ImageTk.PhotoImage(resized_icon)

        item_container = tk.Frame(self.bottom_bar, bg="#25A03D")
        item_container.grid(row=0, column=column, padx=20)

        image_label = tk.Label(item_container, image=photo, bg="#25A03D")
        image_label.image = photo
        image_label.pack()

        text_label = tk.Label(item_container, text=label_text, bg="#25A03D", fg="black")
        text_label.pack()

        # Bind the click event to the image label
        image_label.bind("<Button-1>", click_function)

    def search_clicked(self, event):
        print("Search clicked")
        #switch to search page
        self.master.switch_to_def_search_page()
        #move to search page
        

    def for_you_clicked(self, event):
        print("For You clicked")
        self.master.switch_to_for_you_page()
        

    def my_events_clicked(self, event):
        print("My Events clicked")
        self.master.switch_to_my_events_page()

    def profile_clicked(self, event):
        print("Profile clicked")
        self.master.switch_to_profile_page()

    def perform_search(self):
        search_query = self.search_bar.get()
        self.master.switch_to_search_page(search_query)




# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = EventPageInfo(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()
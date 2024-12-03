import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json
import random

class ForYouPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.current_page = None
        self.create_widgets()


    def create_widgets(self):
        self.configure(bg="#F5F5F5")  # Set background for the entire page
        self.master.title("For You")
        self.master.geometry("390x934")  # iPhone size

        # Styling
        self.bg_color = "#F5F5F5"
        self.btn_color = "#D3D3D3"  # Light gray for button

        total_height = 844
        top_bar_height = 90
        bottom_bar_height = 90
        scrollable_height = total_height - (top_bar_height + bottom_bar_height)

        # Green bar at the top
        self.green_bar = tk.Frame(self, bg="#25A03D", height=top_bar_height)
        self.green_bar.pack(fill="x", side="top")
        self.green_bar.pack_propagate(False)

        self.title = tk.Label(self.green_bar, text="For You", font=("Helvetica", 24, "bold"), fg="white", bg="#25A03D")
        self.title.pack(expand=True)

        # Search Section
        search_frame = tk.Frame(self, bg=self.bg_color)
        search_frame.pack(pady=10, padx=10, fill="x")

        search_frame.grid_columnconfigure(0, weight=1)
        search_frame.grid_columnconfigure(1, weight=0)

        self.search_bar = ttk.Entry(search_frame, font=("Helvetica", 12))
        self.search_bar.grid(row=0, column=0, sticky="ew", padx=(0, 5), ipady=8)

        self.search_button = tk.Button(
            search_frame, text="Search", bg=self.btn_color, font=("Helvetica", 12, "bold"),
            relief="flat", fg="black", activebackground="#C0C0C0", command=self.perform_search
        )
        self.search_button.grid(row=0, column=1, sticky="ew", ipadx=10, ipady=8)

        # Bottom Bar
        self.bottom_bar = tk.Frame(self, bg="#25A03D", height=bottom_bar_height)
        self.bottom_bar.pack(side="bottom", fill="x")
        self.bottom_bar.pack_propagate(False)

        self.create_bottom_bar()

        # Scrollable Section
        scrollable_section = tk.Frame(self, bg=self.bg_color, height=scrollable_height)
        scrollable_section.pack(fill="both", expand=True)

        self.scrollable_canvas = tk.Canvas(scrollable_section, bg=self.bg_color, height=scrollable_height)
        self.scrollable_frame = ttk.Frame(self.scrollable_canvas)
        self.scrollable_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(scrollable_section, orient="vertical", command=self.scrollable_canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollable_canvas.configure(yscrollcommand=self.scrollbar.set)

        #now we pick 10 random events to display from introSurveyAnswer.json
        random_events = self.get_random_events("introSurveyAnswer.json", 10)
    
        #now we display the events

        for i, event in enumerate(random_events):
            # Create the frame for each event
            event_frame = tk.Frame(self.scrollable_frame, bg=self.bg_color)
            event_frame.pack(fill="x", pady=5, padx=10)

            # Load and resize the event image
            image = Image.open(event["image_path"])
            resized_image = image.resize((100, 100), Image.LANCZOS)
            photo = ImageTk.PhotoImage(resized_image)

            # Create and pack the image label on the left side
            image_label = tk.Label(event_frame, image=photo, bg=self.bg_color)
            image_label.image = photo
            image_label.pack(side="left", padx=(0, 10))

            # Bind the click event to the image label
            image_label.bind("<Button-1>", lambda e, event=event: self.on_image_click(e, event))

            # Create a frame for the event info (name, date, time, location)
            event_info = tk.Frame(event_frame, bg=self.bg_color)
            event_info.pack(fill="both", expand=True)

            # Add event name
            tk.Label(
                event_info, 
                text=event["name"], 
                font=("Helvetica", 14), 
                bg=self.bg_color, 
                wraplength=350,  # Wrap text at 350 pixels wide
                justify="left"
            ).pack(anchor="w")

            # Add event date
            tk.Label(
                event_info, 
                text=f"Date: {event['local_date']}", 
                font=("Helvetica", 12), 
                bg=self.bg_color
            ).pack(anchor="w")

            # Add event time
            tk.Label(
                event_info, 
                text=f"Time: {event['local_time']}", 
                font=("Helvetica", 12), 
                bg=self.bg_color
            ).pack(anchor="w")

            # Add event location (venue name, city, state)
            tk.Label(
                event_info, 
                text=f"Location: {event['venue_name']}, {event['venue_city']}, {event['venue_state']}", 
                font=("Arial", 12), 
                bg=self.bg_color
            ).pack(anchor="w")
        


        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.scrollable_canvas.configure(scrollregion=self.scrollable_canvas.bbox("all"))
        )

    def on_image_click(self, event, event_data):
        print(f"Image clicked for event: {event_data['name']}")
        self.master.switch_to_event_info_pageTwo(event_data)
        # You can replace this with any action you'd like, for example:

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

    def get_random_events(self, file_path, num_events=25):
    # Open and load the JSON data from the file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Extract the event details from the loaded data
        events = list(data.values())  # Convert the dictionary to a list of events
        
        # Create a set to track event names to ensure uniqueness
        unique_events = []
        seen_event_names = set()
        
        # Filter out events with duplicate names
        for event in events:
            if event['name'] not in seen_event_names:
                unique_events.append(event)
                seen_event_names.add(event['name'])
        
        # Select num_events random events (if there are enough unique events)
        selected_events = random.sample(unique_events, min(num_events, len(unique_events)))
        
        return selected_events  # Return the list of selected events

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
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ForYouPage(master=root)
#     app.pack(fill="both", expand=True)
#     root.mainloop()
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json
import os
import webbrowser

class MyEventsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.current_page = None
        self.create_widgets()


    def create_widgets(self):
        self.configure(bg="#F5F5F5")  # Set background for the entire page
        self.master.title("My Events")
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

        self.title = tk.Label(self.green_bar, text="My Events", font=("Helvetica", 24, "bold"), fg="white", bg="#25A03D")
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


        email = self.master.email
        my_events = []

        # Open the JSON file and load its content
        with open("myEvents.json", "r") as file:
            data = json.load(file)

            # Search for the user object by email
            user = next((item for item in data if item.get("email") == email), None)

            if user and "favorites" in user:
                # If the user is found and has favorites, retrieve them
                my_events = user["favorites"]
            else:
                # Handle the case where the user has no favorites
                my_events = []



        #now check if there are any events
        if len(my_events) == 0:
            no_events_label = tk.Label(
            self.scrollable_frame,
            text="No events to display, start adding to your favorites!",
            font=("Helvetica", 16),
            bg=self.bg_color,
            wraplength=265,
            justify="center"  # Center-align the text within the label
            )
            no_events_label.pack(pady=60, padx=65, expand=True)  # Expand ensures it uses extra space for centering

        else:
            

            #clear whatver is in the scrollable frame
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
 

            for event in my_events:
                event_frame = tk.Frame(self.scrollable_frame, bg=self.bg_color, relief="solid", bd=1)
                event_frame.pack(fill="x", padx=10, pady=10)

            
                eventPic = Image.open(f"saved_events_pics/{event['name']}.png")
                resized_eventPic = eventPic.resize((100, 90), Image.LANCZOS)
                Eventphoto = ImageTk.PhotoImage(resized_eventPic)
                
                # Save reference to prevent garbage collection
                event_photo_label = tk.Label(event_frame, image=Eventphoto, bg=self.bg_color)
                event_photo_label.image = Eventphoto
                event_photo_label.pack(side="left", padx=10)
            

                event_name = tk.Label(event_frame, text=event["name"], font=("Helvetica", 16, "bold"), bg=self.bg_color, wraplength=200)
                event_name.pack(pady=(10, 0))

                event_date = tk.Label(event_frame, text=event["local_date"], font=("Helvetica", 12), bg=self.bg_color, wraplength=200)
                event_date.pack(pady=(5, 0))

                event_time = tk.Label(event_frame, text=event["local_time"], font=("Helvetica", 12), bg=self.bg_color, wraplength=200)
                event_time.pack(pady=(5, 0))

                venue_name = tk.Label(event_frame, text=event["venue_name"], font=("Helvetica", 12), bg=self.bg_color, wraplength=200)
                venue_name.pack(pady=(5, 0))

                venue_city = tk.Label(event_frame, text=event["venue_city"], font=("Helvetica", 12), bg=self.bg_color, wraplength=200)
                venue_city.pack(pady=(5, 0))

                venue_state = tk.Label(event_frame, text=event["venue_state"], font=("Helvetica", 12), bg=self.bg_color, wraplength=200)
                venue_state.pack(pady=(5, 0))

                # Remove button with red background
                remove_button = tk.Button(
                    event_frame, text="Remove", bg="red", fg="white", font=("Helvetica", 12, "bold"),
                    relief="flat", activebackground="darkred",
                    command=lambda event=event, frame=event_frame: self.remove_event(event, frame)
                )
                remove_button.pack(side="right", padx=10, pady=10)

                #add a buy ticket button
                buy_ticket_button = tk.Button(
                    event_frame, text="Buy Ticket", bg="blue", fg="white", font=("Helvetica", 12, "bold"),
                    relief="flat", activebackground="darkred",
                    command=lambda event=event: self.buy_ticket(event)
                )
                buy_ticket_button.pack(side="right", padx=10, pady=10)


    
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.scrollable_canvas.configure(scrollregion=self.scrollable_canvas.bbox("all"))
        )

        # Bottom Bar
        self.bottom_bar = tk.Frame(self, bg="#25A03D", height=bottom_bar_height)
        self.bottom_bar.pack(side="bottom", fill="x")
        self.bottom_bar.pack_propagate(False)

        self.create_bottom_bar()

    def buy_ticket(self, event):
        print(f"Buying ticket for event: {event['name']}")
        # Open the event URL in the browser
        webbrowser.open(event["event_url"])

    def remove_event(self, event, frame):
        """Removes the event and deletes its image from the folder."""
        try:
            # Remove the event from the JSON file
            email = self.master.email
            with open("myEvents.json", "r") as file:
                data = json.load(file)

            # Find the user and remove the event
            user = next((item for item in data if item.get("email") == email), None)
            if user and "favorites" in user:
                user["favorites"] = [fav for fav in user["favorites"] if fav["name"] != event["name"]]

            with open("myEvents.json", "w") as file:
                json.dump(data, file, indent=4)

            # Delete the event image
            image_path = f"saved_events_pics/{event['name']}.png"
            if os.path.exists(image_path):
                os.remove(image_path)

            # Remove the event frame from the UI
            frame.destroy()

            print(f"Event '{event['name']}' removed successfully.")

            #check if there are any events left
            if len(user["favorites"]) == 0:
                #if there are no events left, display a message
                no_events_label = tk.Label(
                    self.scrollable_frame,
                    text="No events to display, start adding to your favorites!",
                    font=("Helvetica", 16),
                    bg=self.bg_color,
                    wraplength=265,
                    justify="center"  # Center-align the text within the label
                )
                no_events_label.pack(pady=60, padx=65, expand=True)  # Expand ensures it uses extra space for centering
        except Exception as e:
            print(f"Error removing event: {e}")

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
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MyEventsPage(master=root)
#     app.pack(fill="both", expand=True)
#     root.mainloop()
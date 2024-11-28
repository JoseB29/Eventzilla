import os  # To list files in the folder
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class SearchPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Search")
        self.master.geometry("390x934")  # iPhone size

        # Styling
        self.bg_color = "#F5F5F5"
        self.btn_color = "#D3D3D3"  # Light gray for button
        self.master.configure(bg=self.bg_color)

        total_height = 844
        top_bar_height = 90
        bottom_bar_height = 90
        scrollable_height = total_height - (top_bar_height + bottom_bar_height)

        # Add a green bar at the top of the screen
        self.green_bar = tk.Frame(self.master, bg="#25A03D", height=top_bar_height)
        self.green_bar.pack(fill="x", side="top")
        self.green_bar.pack_propagate(False)

        self.title = tk.Label(self.green_bar, text="Search", font=("Odibee Sans", 24, "bold"), fg="white", bg="#25A03D")
        self.title.pack(expand=True)

        # Search Section
        search_frame = tk.Frame(self.master, bg=self.bg_color)
        search_frame.pack(pady=10, padx=10, fill="x")

        search_frame.grid_columnconfigure(0, weight=1)
        search_frame.grid_columnconfigure(1, weight=0)

        self.search_bar = ttk.Entry(search_frame, font=("Arial", 12))
        self.search_bar.grid(row=0, column=0, sticky="ew", padx=(0, 5), ipady=8)

        self.search_button = tk.Button(search_frame, text="Search", bg=self.btn_color, font=("Arial", 12, "bold"),
                                       relief="flat", fg="black", activebackground="#C0C0C0", command=self.perform_search)
        self.search_button.grid(row=0, column=1, sticky="ew", ipadx=10, ipady=8)

        # Scrollable Section (takes up the space between top and bottom bars)
        scrollable_section = tk.Frame(self.master, bg=self.bg_color, height=scrollable_height)
        scrollable_section.pack(fill="both", expand=True)

        self.scrollable_canvas = tk.Canvas(scrollable_section, bg=self.bg_color, height=scrollable_height)
        self.scrollable_frame = ttk.Frame(self.scrollable_canvas)
        self.scrollable_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(scrollable_section, orient="vertical", command=self.scrollable_canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollable_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.scrollable_canvas.configure(scrollregion=self.scrollable_canvas.bbox("all"))
        )

        # Load images from event_images folder
        self.load_images()

        # Bottom Bar (green bar at the bottom)
        self.bottom_bar = tk.Frame(self.master, bg="#25A03D", height=bottom_bar_height)
        self.bottom_bar.pack(side="bottom", fill="x")  # Positioned at the bottom
        self.bottom_bar.pack_propagate(False)

        # Add bottom bar content
        self.create_bottom_bar()

    def load_images(self):
        # Define the path to your images folder
        event_images_path = 'event_images'

        # List all image files in the event_images directory
        for image_file in os.listdir(event_images_path):
            image_path = os.path.join(event_images_path, image_file)

            if os.path.isfile(image_path) and image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Open and resize the image
                image = Image.open(image_path)
                resized_image = image.resize((350, 200), Image.LANCZOS)
                photo = ImageTk.PhotoImage(resized_image)

                # Create an image label and add it to the scrollable frame
                image_label = tk.Label(self.scrollable_frame, image=photo)
                image_label.image = photo  # Keep a reference to avoid garbage collection
                image_label.pack(pady=10)

    def create_bottom_bar(self):
        # Use grid layout for even distribution of bottom bar items
        self.bottom_bar.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Add icons and text labels
        self.add_bottom_bar_item("appElements\\magnifyingIconMagnifying.webp", "Search", 0)
        self.add_bottom_bar_item("appElements\\for_you_logo.png", "For You", 1)
        self.add_bottom_bar_item("appElements\\ticketLogo.png", "My Events", 2)
        self.add_bottom_bar_item("appElements\\profile_icon.webp", "Profile", 3)

    def add_bottom_bar_item(self, image_path, label_text, column):
        icon = Image.open(image_path)
        resized_icon = icon.resize((50, 50), Image.LANCZOS)
        photo = ImageTk.PhotoImage(resized_icon)

        # Create container for each bottom bar item
        item_container = tk.Frame(self.bottom_bar, bg="#25A03D")
        item_container.grid(row=0, column=column, padx=20)

        image_label = tk.Label(item_container, image=photo, bg="#25A03D")
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack()

        text_label = tk.Label(item_container, text=label_text, bg="#25A03D", fg="black")
        text_label.pack()

    def perform_search(self):
        # Handle search button click
        search_query = self.search_bar.get()
        print(f"Search Query: {search_query}")

        # Clear everything in the page
        for widget in self.master.winfo_children():
            widget.destroy()

        #go to the search page
        self.master.show_search_page()


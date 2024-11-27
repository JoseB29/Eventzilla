import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class DiscoverPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Discover")
        self.master.geometry("390x844")  # iPhone size

        # Styling
        self.bg_color = "#F5F5F5"
        self.btn_color = "#D3D3D3"  # Light gray for button
        self.master.configure(bg=self.bg_color)

        # Add a green bar at the top of the screen
        self.green_bar = tk.Frame(self.master, bg="#25A03D", height=90)
        self.green_bar.pack(fill="x", side="top")
        self.green_bar.pack_propagate(False)

        # Add a title at the center of the top green bar
        self.title = tk.Label(self.green_bar, text="Discover", font=("Odibee Sans", 24, "bold"), fg="white", bg="#25A03D")
        self.title.pack(expand=True)

        # Add a frame for the search bar and button
        search_frame = tk.Frame(self.master, bg=self.bg_color)
        search_frame.pack(pady=10, padx=10, fill="x")

        # Configure grid layout for responsive sizing
        search_frame.grid_columnconfigure(0, weight=1)
        search_frame.grid_columnconfigure(1, weight=0)

        # Add a search bar
        self.search_bar = ttk.Entry(search_frame, font=("Arial", 12))
        self.search_bar.grid(row=0, column=0, sticky="ew", padx=(0, 5), ipady=8)  # Stretch horizontally and add padding

        # Add a search button
        self.search_button = tk.Button(search_frame, text="Search", bg=self.btn_color, font=("Arial", 12, "bold"),
                                       relief="flat", fg="black", activebackground="#C0C0C0", command=self.perform_search)
        self.search_button.grid(row=0, column=1, sticky="ew", ipadx=10, ipady=8)  # Stretch horizontally

        # Create a frame to contain the scrollable section and its scrollbar
        scrollable_section = tk.Frame(self.master, bg=self.bg_color)
        scrollable_section.pack(padx=10, pady=(0, 10), fill="both", expand=True)  # Make it expand vertically

        # Add a scrollable canvas inside the frame
        self.scrollable_canvas = tk.Canvas(scrollable_section, bg=self.bg_color)
        self.scrollable_frame = ttk.Frame(self.scrollable_canvas)
        self.scrollable_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_canvas.pack(side="left", fill="both", expand=True)

        # Add a scrollbar next to the canvas
        self.scrollbar = ttk.Scrollbar(scrollable_section, orient="vertical", command=self.scrollable_canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollable_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Add some sample content to the scrollable frame
        for i in range(20):
            tk.Label(self.scrollable_frame, text=f"Event {i + 1}", font=("Arial", 14), bg=self.bg_color).pack(pady=5, padx=10)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.scrollable_canvas.configure(scrollregion=self.scrollable_canvas.bbox("all"))
        )

        # Create a bottom bar frame
        self.bottom_bar = tk.Frame(self.master, bg="#25A03D", height=90)
        self.bottom_bar.pack(fill="x", side="bottom")
        self.bottom_bar.pack_propagate(False)

        # Add bottom bar icons
        self.create_bottom_bar()

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


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DiscoverPage(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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

        self.title = tk.Label(self.green_bar, text="My Events", font=("Odibee Sans", 24, "bold"), fg="white", bg="#25A03D")
        self.title.pack(expand=True)

        # Search Section
        search_frame = tk.Frame(self, bg=self.bg_color)
        search_frame.pack(pady=10, padx=10, fill="x")

        search_frame.grid_columnconfigure(0, weight=1)
        search_frame.grid_columnconfigure(1, weight=0)

        self.search_bar = ttk.Entry(search_frame, font=("Arial", 12))
        self.search_bar.grid(row=0, column=0, sticky="ew", padx=(0, 5), ipady=8)

        self.search_button = tk.Button(
            search_frame, text="Search", bg=self.btn_color, font=("Arial", 12, "bold"),
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


        #sample filling of the scrollable frame
        for i in range(20):
            tk.Label(self.scrollable_frame, text=f"Event {i + 1}", font=("Arial", 14), bg=self.bg_color).pack(pady=5, padx=10)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.scrollable_canvas.configure(scrollregion=self.scrollable_canvas.bbox("all"))
        )

        # Bottom Bar
        self.bottom_bar = tk.Frame(self, bg="#25A03D", height=bottom_bar_height)
        self.bottom_bar.pack(side="bottom", fill="x")
        self.bottom_bar.pack_propagate(False)

        self.create_bottom_bar()

    def create_bottom_bar(self):
        self.bottom_bar.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.add_bottom_bar_item("appElements\\magnifyingIconMagnifying.webp", "Search", 0)
        self.add_bottom_bar_item("appElements\\for_you_logo.png", "For You", 1)
        self.add_bottom_bar_item("appElements\\ticketLogo.png", "My Events", 2)
        self.add_bottom_bar_item("appElements\\profile_icon.webp", "Profile", 3)

    def add_bottom_bar_item(self, image_path, label_text, column):
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

    def perform_search(self):
        search_query = self.search_bar.get()
        self.master.switch_to_search_page(search_query)




# Run the app
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MyEventsPage(master=root)
#     app.pack(fill="both", expand=True)
#     root.mainloop()
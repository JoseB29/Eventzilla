import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class EventPageInfo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        # self.current_page = None
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
        scrollable_height = total_height - (top_bar_height + bottom_bar_height)

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
        self.title = tk.Label(self.green_bar, text="Event Details", font=("Odibee Sans", 24, "bold"), fg="white", bg="#25A03D")
        self.title.pack(expand=True)

        # Bottom Bar
        self.bottom_bar = tk.Frame(self, bg="#25A03D", height=bottom_bar_height)
        self.bottom_bar.pack(side="bottom", fill="x")
        self.bottom_bar.pack_propagate(False)

        self.create_bottom_bar()

    def arrow_clicked(self, event):
        print("Arrow clicked!")
        # Add functionality, e.g., navigate back or close the page
        # self.master.switch_to_previous_page()



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
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json


class ProfilePage(tk.Frame):
    def __init__(self, master=None, email=None):
        super().__init__(master)
        self.master = master
        self.email = email
        self.current_page = None
        self.create_widgets()

    def create_widgets(self):
        self.configure(bg="#F5F5F5")  # Set background for the entire page
        self.master.title("Profile Page")
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

        self.title = tk.Label(self.green_bar, text="My Account", font=("Odibee Sans", 24, "bold"), fg="white", bg="#25A03D")
        self.title.pack(expand=True)

        username = self.get_username_by_email(self.email)
        self.username_label = tk.Label(self.green_bar, text=username, font=("Odibee Sans", 15, "bold"), fg="white", bg="#25A03D", anchor="w")
        self.username_label.pack(fill="x", side="top", anchor="w", padx=10)

        self.email_label = tk.Label(self.green_bar, text=self.email, font=("Odibee Sans", 15), fg="white", bg="#25A03D", anchor="w")
        self.email_label.pack(fill="x", side="top", anchor="w", padx=10)

        # Notification Section
        notification_frame = tk.Frame(self, bg=self.bg_color)
        notification_frame.pack(pady=10, padx=10, fill="x")

        self.notification_label = tk.Label(notification_frame, text="Notifications", font=("Helvetica", 15, "bold"), fg="black", anchor="w")
        self.notification_label.pack(fill="x", side="top", anchor="w", padx=10)

        # add My Notificantions button
        self.notification_button = tk.Button(
            notification_frame, text="My Notifications", bg=self.btn_color, font=("Arial", 12, "bold"),
            relief="flat", fg="black", activebackground="#C0C0C0"
        )
        self.notification_button.pack(fill="x", side="top", anchor="w", padx=10, pady=5)

        # Account Management Section

        # Privacy and Security Section

        # Sign out button

 
        # Bottom Bar
        self.bottom_bar = tk.Frame(self, bg="#25A03D", height=bottom_bar_height)
        self.bottom_bar.pack(side="bottom", fill="x")
        self.bottom_bar.pack_propagate(False)

        self.create_bottom_bar()
    
    def get_username_by_email(self, email):
        try:
            with open("users.json", "r") as f:
                users = json.load(f)
                user = next((u for u in users if u["email"] == email), None)
                if user:
                    return user["username"]
        except (json.JSONDecodeError, FileNotFoundError):
            pass
        return "Failed to get username"

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
    app = ProfilePage(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()
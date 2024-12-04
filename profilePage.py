import json
import tkinter as tk
from tkinter import ttk
from accountManagement import AccountManagementScreen 
from Settings import SettingsScreen
from PIL import Image, ImageTk

class ProfilePage (tk.Frame):
    def __init__(self, master=None, email=None):
        super().__init__(master)
        self.master = master
        self.email = email
        self.current_screen = None
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Profile Page")
        self.master.geometry("390x934")  # iPhone size 

        # Styling
        self.bg_color = "#F5F5F5"
        self.btn_color = "#25A03D"
        self.master.configure(bg=self.bg_color)
        bottom_bar_height = 90

        # Create a frame for the create account form
        self.frame = tk.Frame(self, bg="white", padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        title_frame = tk.Frame(self, bg="green")
        title_frame.pack(fill=tk.X)

        self.title = tk.Label(title_frame, text="My Account", font=("Helvetica", 24, "bold"), fg="white", bg="green")
        self.title.pack(expand=True)

        username = self.get_username_by_email(self.email)
        self.username_label = tk.Label(title_frame, text=username, font=("Helvetica", 15, "bold"), fg="white", bg="green", anchor="w")
        self.username_label.pack(fill="x", side="top", anchor="w", padx=10)

        self.email_label = tk.Label(title_frame, text=self.email, font=("Helvetica", 15), fg="white", bg="green", anchor="w")
        self.email_label.pack(fill="x", side="top", anchor="w", padx=10)

        # Notification Section
        notification_frame = tk.Frame(self, bg=self.bg_color)
        notification_frame.pack(pady=10, padx=10, fill="x")

        self.notification_label = tk.Label(notification_frame, text="Notifications", font=("Helvetica", 15, "bold"), fg="black", anchor="w")
        self.notification_label.pack(fill="x", side="top", anchor="w", padx=10)

        # add My Notificantions button
        self.notification_button = tk.Button(
            notification_frame, text="My Notifications                                                   >", 
            bg="#D3D3D3", font=("Helvetica", 12, "bold"),
            command=self.notification_preferences,
            relief="flat", fg="black", activebackground="#C0C0C0"
        )
        self.notification_button.pack(fill="x", side="top", anchor="w", padx=10, pady=5)

        # Divider
        divider = tk.Frame(self, height=2, bd=1, relief="sunken", bg="#D3D3D3")
        divider.pack(fill="x", padx=10, pady=10)
        
        # Account Management Section
        account_management_frame = tk.Frame(self, bg=self.bg_color)
        account_management_frame.pack(pady=10, padx=10, fill="x")

        self.account_management_label = tk.Label(account_management_frame, text="Account Management", font=("Helvetica", 15, "bold"), fg="black", anchor="w")
        self.account_management_label.pack(fill="x", side="top", anchor="w", padx=10)

        # account management button
        self.account_management_button = tk.Button(
            account_management_frame, text="Manage Account                                                  >", bg="#D3D3D3", font=("Helvetica", 12, "bold"),
            relief="flat", fg="black", activebackground="#C0C0C0", command=self.open_account_management_screen
        )
        self.account_management_button.pack(fill="x", side="top", anchor="w", padx=10, pady=5)


        # Sign out button
        self.sign_out_button = tk.Button(
            self, text="Sign Out", font=("Helvetica", 12, "bold"), 
            fg="red", relief="flat",
            command=self.sign_out
        )
        self.sign_out_button.pack(pady=10)

        # Bottom Bar
        self.bottom_bar = tk.Frame(self, bg="#25A03D", height=bottom_bar_height)
        self.bottom_bar.pack(side="bottom", fill="x")
        self.bottom_bar.pack_propagate(False)

        self.create_bottom_bar()

    def open_account_management_screen(self):
        if self.current_screen:
            self.current_screen.destroy()  # Remove the current screen
        self.current_screen = AccountManagementScreen(master=self.master, email=self.email)
        self.current_screen.pack(fill="both", expand=True)
        self.destroy()  # Destroy the profile page

    def sign_out(self):
        self.master.show_screen1()  # Navigate to the sign-in screen
        self.destroy()  # Destroy the profile page
    
    def notification_preferences(self):
        self.master.show_screen6()  # Navigate to the notification preferences screen
        self.destroy()  # Destroy the profile page


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
        self.add_bottom_bar_item("appElements/magnifyingIconMagnifying.webp", "Search", 0, self.search_clicked)
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

    def for_you_clicked(self, event):
        print("For You clicked")
        self.master.switch_to_for_you_page()
    
    def search_clicked(self, event):
        print("Search clicked")
        #switch to search page
        self.master.switch_to_def_search_page()
        #move to search page

    def my_events_clicked(self, event):
        print("My Events clicked")
        self.master.switch_to_my_events_page()

    def profile_clicked(self, event):
        print("Profile clicked")
        self.master.switch_to_profile_page()

    def perform_search(self):
        search_query = self.search_bar.get()
        self.master.switch_to_search_page(search_query)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProfilePage(master=root)
    app.pack(fill="both", expand=True)
    app.mainloop()
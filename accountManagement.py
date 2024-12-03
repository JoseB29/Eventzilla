import tkinter as tk
from tkinter import messagebox


class AccountManagementScreen(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master, width=390, height=964)  # Set fixed width and height
        self.master = master
        self.controller = controller

        # TODO: Incorporate user's actual information they entered earlier 
        self.user_data = {
            "username": "user123",
            "email": "user@example.com",
            "name": "John Doe",
            "phone": "123-456-7890",
        }

        # Ensure fixed screen size
        self.master.title("Account Management")
        self.master.geometry("390x964")
        self.master.resizable(False, False)  # Disable resizing
        self.create_widgets()

    def create_widgets(self):
        # Header
        tk.Label(
            self,
            text="Account Management",
            font=("Helvetica", 18, "bold"),
            bg="#4CAF50",
            fg="white",
            anchor="center",
        ).pack(fill="x", pady=10)

        # Section: Account Information
        tk.Label(self, text="Your Account Information:", font=("Helvetica", 12, "bold")).pack(pady=5)
        self.info_frame = tk.Frame(self)
        self.info_frame.pack(pady=10)
        self.display_user_info()

        # Buttons for Account Management Options
        button_style = {"font": ("Helvetica", 12), "bg": "#f5f5f5", "fg": "black", "width": 30}
        #tk.Button(self, text="Change Password", command=self.change_password, **button_style).pack(pady=5)
        tk.Button(self, text="Update Username", command=self.update_username, **button_style).pack(pady=5)
        tk.Button(self, text="Edit Personal Info", command=self.edit_personal_info, **button_style).pack(pady=5)

        # Footer Section with Back Button
        tk.Button(
            self,
            text="Back to Settings",
            font=("Helvetica", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            command=self.controller.open_settings_screen,
        ).pack(pady=20)

    def display_user_info(self):
        """Displays user information in the info frame."""
        for widget in self.info_frame.winfo_children():
            widget.destroy()  # Clear the frame

        for key, value in self.user_data.items():
            tk.Label(self.info_frame, text=f"{key.capitalize()}: {value}", font=("Helvetica", 10)).pack(anchor="w", padx=10)

    
    def update_username(self):
        """Opens a window to update the username."""
        def submit_username():
            new_username = username_entry.get()
            if new_username.strip():
                self.user_data["username"] = new_username.strip()
                messagebox.showinfo("Success", "Username updated successfully!")
                self.display_user_info()
                username_window.destroy()
            else:
                messagebox.showerror("Error", "Username cannot be empty!")

        username_window = tk.Toplevel(self)
        username_window.title("Update Username")
        username_window.geometry("300x150")
        username_window.resizable(False, False)

        tk.Label(username_window, text="New Username:", font=("Helvetica", 10)).pack(pady=5)
        username_entry = tk.Entry(username_window, width=30)
        username_entry.pack(pady=5)

        tk.Button(username_window, text="Submit", font=("Helvetica", 10), command=submit_username).pack(pady=10)

    def edit_personal_info(self):
        """Opens a window to edit personal info."""
        def submit_personal_info():
            new_email = email_entry.get()
            new_name = name_entry.get()
            new_phone = phone_entry.get()

            # Update user data
            if new_email.strip():
                self.user_data["email"] = new_email.strip()
            if new_name.strip():
                self.user_data["name"] = new_name.strip()
            if new_phone.strip():
                self.user_data["phone"] = new_phone.strip()

            messagebox.showinfo("Success", "Personal information updated successfully!")
            self.display_user_info()
            personal_info_window.destroy()

        personal_info_window = tk.Toplevel(self)
        personal_info_window.title("Edit Personal Info")
        personal_info_window.geometry("300x250")
        personal_info_window.resizable(False, False)

        tk.Label(personal_info_window, text="Email:", font=("Helvetica", 10)).pack(pady=5)
        email_entry = tk.Entry(personal_info_window, width=30)
        email_entry.insert(0, self.user_data["email"])
        email_entry.pack(pady=5)

        tk.Label(personal_info_window, text="Name:", font=("Helvetica", 10)).pack(pady=5)
        name_entry = tk.Entry(personal_info_window, width=30)
        name_entry.insert(0, self.user_data["name"])
        name_entry.pack(pady=5)

        tk.Label(personal_info_window, text="Phone:", font=("Helvetica", 10)).pack(pady=5)
        phone_entry = tk.Entry(personal_info_window, width=30)
        phone_entry.insert(0, self.user_data["phone"])
        phone_entry.pack(pady=5)

        tk.Button(personal_info_window, text="Submit", font=("Helvetica", 10), command=submit_personal_info).pack(pady=10)

        


# if __name__ == "__main__":
#     class Controller:
#         def open_settings_screen(self):
#             print("Navigating back to settings...")

#     root = tk.Tk()
#     app = AccountManagementScreen(master=root, controller=Controller())
#     app.pack(fill="both", expand=True)
#     root.mainloop()
import tkinter as tk
from tkinter import messagebox

class PrivacyAndSecurityScreen(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master, width=390, height=964)  # Set fixed width and height
        self.master = master
        self.controller = controller

        # Ensure fixed screen size
        self.master.title("Privacy And Security")
        self.master.geometry("390x964")
        self.master.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Header
        tk.Label(
            self,
            text="Privacy & Security",
            font=("Helvetica", 18, "bold"),
            bg="#4CAF50",
            fg="white",
            anchor="center",
        ).pack(fill="x", pady=10)

        # Section: Privacy Options
        tk.Label(
            self, text="Manage your security settings:", font=("Helvetica", 12, "bold")
        ).pack(pady=5)

        # Button for Password Change
        tk.Button(
            self,
            text="Change Password",
            font=("Helvetica", 12),
            bg="#f5f5f5",
            fg="black",
            width=30,
            command=self.change_password,
        ).pack(pady=10)

        # Footer Section with Back Button
        tk.Button(
            self,
            text="Back to Settings",
            font=("Helvetica", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            command=self.controller.open_settings_screen,  # Navigate back
        ).pack(pady=20)

    def change_password(self):
        """Opens a window to change the password."""

        def submit_password():
            new_password = password_entry.get()
            confirm_password = confirm_entry.get()
            if new_password == confirm_password:
                messagebox.showinfo("Success", "Password changed successfully!")
                password_window.destroy()
            else:
                messagebox.showerror("Error", "Passwords do not match!")

        password_window = tk.Toplevel(self)
        password_window.title("Change Password")
        password_window.geometry("300x200")
        password_window.resizable(False, False)

        tk.Label(password_window, text="New Password:", font=("Helvetica", 10)).pack(pady=5)
        password_entry = tk.Entry(password_window, show="*", width=30)
        password_entry.pack(pady=5)

        tk.Label(password_window, text="Confirm Password:", font=("Helvetica", 10)).pack(pady=5)
        confirm_entry = tk.Entry(password_window, show="*", width=30)
        confirm_entry.pack(pady=5)

        tk.Button(password_window, text="Submit", font=("Helvetica", 10), command=submit_password).pack(pady=10)

# if __name__ == "__main__":
#     class Controller:
#         def open_settings_screen(self):
#             print("Navigating back to settings...")
#             messagebox.showinfo("Navigation", "Returning to Settings Screen.")

#     root = tk.Tk()
#     app = PrivacyAndSecurityScreen(master=root, controller=Controller())
#     app.pack(fill="both", expand=True)
#     root.mainloop()

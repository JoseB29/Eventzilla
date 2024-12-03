import tkinter as tk
from tkinter import messagebox
from accountManagement import AccountManagementScreen  # Assuming this is in a separate file
from loginMenu import LoginApp  # Import LoginApp for the Log Out functionality


class SettingsScreen(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Settings")
        self.master.geometry("390x934")  # iPhone size dimensions

        # Styling
        self.bg_color = "#F5F5F5"
        self.btn_color = "#25A03D"
        self.master.configure(bg=self.bg_color)

        # Title bar
        title_frame = tk.Frame(self, bg="green")
        title_frame.pack(fill=tk.X)
        title_label = tk.Label(
            title_frame, text="Settings", font=("Helvetica", 16, "bold"), bg="green", fg="white"
        )
        title_label.pack(pady=10)

        # Frame for settings options
        self.frame = tk.Frame(self, bg="white", padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # List of settings options
        options = [
            "Account Management",
            "Privacy & Security",
            "Notification Settings",
            "Customization Settings",
            "Log Out",
        ]

        # Button for each option
        for option in options:
            option_frame = tk.Frame(self.frame, bg="white")
            option_frame.pack(fill="x", pady=(5, 10))
            option_button = tk.Button(
                option_frame,
                text=option + " →",
                font=("Helvetica", 12),
                bg="white",
                anchor="w",
                relief="flat",
                command=lambda opt=option: self.on_option_click(opt),
            )
            option_button.pack(side="left", fill="x")

        

    def on_option_click(self, option):
        """Handles clicks on settings options."""
        if option == "Account Management":
            self.controller.open_account_management_screen()
        elif option == "Privacy & Security":
            self.controller.open_privacy_and_security_screen()
        elif option == "Log Out":  # Navigate to the Login Screen
            self.controller.open_login_screen()
        else:
            messagebox.showinfo("Info", f"{option} is not implemented yet.")

class App2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App")
        self.geometry("390x934")
        self.current_screen = None

        # Initialize with Settings screen
        self.open_settings_screen()

    def open_settings_screen(self):
        if self.current_screen:
            self.current_screen.destroy()  # Remove the current screen
        self.current_screen = SettingsScreen(master=self, controller=self)
        self.current_screen.pack(fill="both", expand=True)

    def open_account_management_screen(self):
        if self.current_screen:
            self.current_screen.destroy()  # Remove the current screen
        self.current_screen = AccountManagementScreen(master=self, controller=self)
        self.current_screen.pack(fill="both", expand=True)

    def open_login_screen(self):
        """Navigate to the login screen."""
        self.destroy()  # Close the current main window
        root = tk.Tk()  # Create a new Tk instance for the login screen
        login_app = LoginApp(master=root)  # Initialize the LoginApp with the new root
        login_app.pack(fill="both", expand=True)
        root.mainloop()  # Start the login app's event loop

    def open_privacy_and_security_screen(self):
        if self.current_screen:
            self.current_screen.destroy()  # Remove the current screen
        from privacyAndSecurity import PrivacyAndSecurityScreen  # Import the screen here
        self.current_screen = PrivacyAndSecurityScreen(master=self, controller=self)
        self.current_screen.pack(fill="both", expand=True)
        


if __name__ == "__main__":
    app = App2()
    app.mainloop()

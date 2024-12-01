import tkinter as tk
from loginMenu import LoginApp
from Survey import QuestionnaireApp
from main import App

class SettingsScreen(tk.Frame):
    def __init__(self, master=None, app_instance=None):
        super().__init__(master)
        self.master = master   
        self.app = app_instance   
        self.current_screen = None   
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Settings")
        self.master.geometry("390x934")  # iPhone size

        # Styling
        self.bg_color = "#F5F5F5"
        self.btn_color = "#25A03D"
        self.master.configure(bg=self.bg_color)

        # Frame for settings form
        self.frame = tk.Frame(self, bg="white", padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title bar
        title_frame = tk.Frame(self, bg="green")
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(title_frame, text="Settings", font=("Helvetica", 16, "bold"), bg="green", fg="white")
        title_label.pack(pady=10)

        # List of settings options
        options = [
            "Account Management",
            "Privacy & Security",
            "Notification Settings",
            "Customization Settings",   
            "Log Out"
        ]

        # Button for each option
        for option in options:
            option_frame = tk.Frame(self.frame, bg="white")
            option_frame.pack(fill="x", pady=(5, 10))
            option_button = tk.Button(option_frame, text=option + " →", font=("Helvetica", 12), bg="white", anchor="w", relief="flat",
                                      command=lambda opt=option: self.on_option_click(opt))
            option_button.pack(side="left", fill="x")

        # Done button
        self.done_button = tk.Button(self.frame, text="Done", bg=self.btn_color, fg="white", command=self.close_settings)
        self.done_button.pack(fill="x", pady=(10, 0))

    # Actions to take when an option is clicked 
    def on_option_click(self, option):
        print(f"Clicked on the {option} option")

        # Specific behavior for each option
        if option == "Account Management":
            print("Navigating to Account Management screen...")

        elif option == "Privacy & Security":
            print("Navigating to Privacy & Security screen...")

        elif option == "Notification Settings":
            print("Navigating to Notification Settings screen...")

        elif option == "Customization Settings":
            print("Navigating to Customization Settings screen...")
            self.destroy_settings_screen()
            self.open_survey()

        elif option == "Log Out":
            print("Logging out...")
            self.destroy_settings_screen()
            app = App()

    # Destroy the settings screen
    def destroy_settings_screen(self):
        print("Destroying settings screen")
        self.destroy()   

    def logout(self):
        self.current_screen = App()

    # Opens the survey screen  
    def open_survey(self):
        self.current_screen = QuestionnaireApp(master=self.master)   
        self.current_screen.pack(fill="both", expand=True)

    def close_settings(self):
        print("Settings closed")  
        self.master.quit()   

# if __name__ == "__main__":
#     root = tk.Tk()

#     settings_screen = SettingsScreen(master=root)   
#     settings_screen.pack(fill="both", expand=True)   
#     root.mainloop()

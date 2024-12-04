import tkinter as tk
import json
import os

class SettingsScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.load_preferences()

    def create_widgets(self):
        self.master.title("Notification Preferences")
        self.master.geometry("390x934")  # iPhone size 

        # Styling
        self.bg_color = "#F5F5F5"
        self.btn_color = "#25A03D"
        self.master.configure(bg=self.bg_color)
        bottom_bar_height = 90

        # Create a frame for the notification preferences form
        self.container = tk.Frame(self, bg="white", padx=20, pady=20)
        self.container.place(relx=0.5, rely=0.5, anchor="center")

        title_frame = tk.Frame(self, bg="green")
        title_frame.pack(fill=tk.X)

        self.title = tk.Label(title_frame, text="Notification Preferences", font=("Helvetica", 24, "bold"), fg="white", bg="green")
        self.title.pack(expand=True)

        # Show notification preferences question
        self.answers = {}
        self.container = tk.Frame(self, bg="white")
        self.container.pack(fill="both", expand=True)

        self.container.configure(bg="white")
        tk.Label(self.container, text="Question 5/5", bg="#88c999", fg="white", font=("Arial", 16, "bold"), height=2).pack(fill="x")
        tk.Label(self.container, text="Set your notification preferences:", bg="white", fg="black", font=("Arial", 14, "bold")).pack(pady=10)

        self.price_tracking_var = tk.IntVar()
        tk.Checkbutton(
            self.container,
            text="Enable price tracking notifications",
            variable=self.price_tracking_var,
            bg="white",
            font=("Arial", 14, "bold"),
            fg="black"
        ).pack(anchor='w', pady=5)

        tk.Label(self.container, text="Frequency of Basic Notifications:", bg="white", fg="black", font=("Arial", 14, "bold")).pack(pady=5)
        self.notification_frequency = tk.StringVar(value="Once a Week")
        for frequency in ["Once a Month", "Once a Week", "Daily"]:
            tk.Radiobutton(
                self.container,
                text=frequency,
                variable=self.notification_frequency,
                value=frequency,
                bg="white",
                font=("Arial", 14, "bold"),
                fg="black"
            ).pack(anchor='w')

        tk.Label(self.container, text="Reminders for Favorited Events:", bg="white", fg="black", font=("Arial", 14, "bold")).pack(pady=5)
        self.reminder_frequency = tk.StringVar(value="Once a Week")
        for reminder in ["Once a Month", "Once a Week", "Daily"]:
            tk.Radiobutton(
                self.container,
                text=reminder,
                variable=self.reminder_frequency,
                value=reminder,
                bg="white",
                font=("Arial", 14, "bold"),
                fg="black"
            ).pack(anchor='w')

        button_frame = tk.Frame(self.container, bg="white")
        button_frame.pack(pady=20)

        # Add a done button
        self.done_button = tk.Button(
            self.container, text="Done", command=self.save_notifications, bg="#88c999", fg="white", font=("Helvetica", 14, "bold")
        )
        self.done_button.pack(pady=20)

    def save_notifications(self):
        self.answers['price_tracking'] = bool(self.price_tracking_var.get())
        self.answers['notification_frequency'] = self.notification_frequency.get()
        self.answers['reminder_frequency'] = self.reminder_frequency.get()

        with open("questionnaire_answers.json", "r+") as f:
            data = json.load(f)
            data.update(self.answers)
            f.seek(0)
            f.truncate()
            json.dump(data, f, indent=4)

        print("Preferences saved successfully")
        self.master.switch_to_profile_page()

    def load_preferences(self):
        if os.path.exists("questionnaire_answers.json"):
            with open("questionnaire_answers.json", "r") as f:
                self.answers = json.load(f)
                self.price_tracking_var.set(int(self.answers.get('price_tracking', 0)))
                self.notification_frequency.set(self.answers.get('notification_frequency', "Daily"))
                self.reminder_frequency.set(self.answers.get('reminder_frequency', "Daily"))

if __name__ == "__main__":
    root = tk.Tk()
    app = SettingsScreen(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()

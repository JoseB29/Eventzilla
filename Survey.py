import tkinter as tk
from tkinter import messagebox

class QuestionnaireApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Event Preferences Questionnaire")
        self.geometry("390x844") #Screen Size For An Iphone
        self.current_question = 0
        self.answers = {}
        self.create_widgets()

    def create_widgets(self):
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.show_question()

    def show_question(self):
        # Clear the container for new content
        for widget in self.container.winfo_children():
            widget.destroy()

        # Navigate to the appropriate question
        if self.current_question == 0:
            self.zip_code_question()
        elif self.current_question == 1:
            self.event_type_question()
        elif self.current_question == 2:
            self.music_genre_question()
        elif self.current_question == 3:
            self.sports_interest_question()
        elif self.current_question == 4:
            self.notification_preferences_question()
        else:
            self.finish()

    def zip_code_question(self):
        tk.Label(self.container, text="What is your zip code?").pack(pady=10)
        self.zip_code_entry = tk.Entry(self.container)
        self.zip_code_entry.pack(pady=5)

        button_frame = tk.Frame(self.container)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Skip", command=self.next_question).pack(side="left", padx=10)
        tk.Button(button_frame, text="Next", command=self.save_zip_code).pack(side="left", padx=10)

    def save_zip_code(self):
        zip_code = self.zip_code_entry.get()
        if zip_code.strip() == "":
            messagebox.showwarning("Input Required", "Please enter your zip code or click Skip.")
        else:
            self.answers['zip_code'] = zip_code
            self.next_question()

    def event_type_question(self):
        tk.Label(self.container, text="Select the types of events you like:").pack(pady=10)

        self.event_vars = {
            "Arts and Museums": tk.IntVar(),
            "Classes": tk.IntVar(),
            "Concerts": tk.IntVar(),
            "Food and Drink": tk.IntVar(),
            "Movies": tk.IntVar(),
            "Sports": tk.IntVar(),
            "Virtual Events": tk.IntVar(),
            "Fitness": tk.IntVar()
        }

        for event, var in self.event_vars.items():
            tk.Checkbutton(self.container, text=event, variable=var).pack(anchor='w')

        button_frame = tk.Frame(self.container)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Skip", command=self.next_question).pack(side="left", padx=10)
        tk.Button(button_frame, text="Next", command=self.save_event_types).pack(side="left", padx=10)

    def save_event_types(self):
        selected_events = [event for event, var in self.event_vars.items() if var.get() == 1]
        self.answers['event_types'] = selected_events
        self.next_question()

    def music_genre_question(self):
        tk.Label(self.container, text="What music genres are you interested in?").pack(pady=10)

        self.music_vars = {
            "Blues/Gospel": tk.IntVar(),
            "Classical": tk.IntVar(),
            "Country": tk.IntVar(),
            "Electronic/Techno": tk.IntVar(),
            "House": tk.IntVar(),
            "Hip Hop/Rap": tk.IntVar(),
            "Indie": tk.IntVar(),
            "Jazz": tk.IntVar(),
            "Latin": tk.IntVar(),
            "Reggae": tk.IntVar(),
            "Metal": tk.IntVar(),
            "Pop": tk.IntVar(),
            "Rock and Roll": tk.IntVar(),
            "R&B/Soul": tk.IntVar(),
            "Opera": tk.IntVar(),
            "Vocal Music": tk.IntVar()
        }

        for genre, var in self.music_vars.items():
            tk.Checkbutton(self.container, text=genre, variable=var).pack(anchor='w')

        button_frame = tk.Frame(self.container)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Skip", command=self.next_question).pack(side="left", padx=10)
        tk.Button(button_frame, text="Next", command=self.save_music_genres).pack(side="left", padx=10)

    def save_music_genres(self):
        selected_genres = [genre for genre, var in self.music_vars.items() if var.get() == 1]
        self.answers['music_genres'] = selected_genres
        self.next_question()

    def sports_interest_question(self):
        tk.Label(self.container, text="What sports are you interested in?").pack(pady=10)

        self.sports_vars = {
            "Soccer": tk.IntVar(),
            "Football": tk.IntVar(),
            "Baseball": tk.IntVar(),
            "Basketball": tk.IntVar(),
            "Tennis": tk.IntVar(),
            "Golf": tk.IntVar(),
            "Hockey": tk.IntVar(),
            "Cycling": tk.IntVar(),
            "Track and Field": tk.IntVar(),
            "Cricket": tk.IntVar(),
            "Wrestling": tk.IntVar(),
            "Martial Arts": tk.IntVar(),
            "Swimming": tk.IntVar(),
            "Volleyball": tk.IntVar(),
            "Esports": tk.IntVar()
        }

        for sport, var in self.sports_vars.items():
            tk.Checkbutton(self.container, text=sport, variable=var).pack(anchor='w')

        button_frame = tk.Frame(self.container)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Skip", command=self.next_question).pack(side="left", padx=10)
        tk.Button(button_frame, text="Next", command=self.save_sports_interests).pack(side="left", padx=10)

    def save_sports_interests(self):
        selected_sports = [sport for sport, var in self.sports_vars.items() if var.get() == 1]
        self.answers['sports_interests'] = selected_sports
        self.next_question()

    def notification_preferences_question(self):
        tk.Label(self.container, text="Set your notification preferences:").pack(pady=10)

        self.price_tracking_var = tk.IntVar()
        tk.Checkbutton(self.container, text="Enable price tracking notifications", variable=self.price_tracking_var).pack(anchor='w')

        tk.Label(self.container, text="Frequency of Basic Notifications:").pack(pady=5)
        self.notification_frequency = tk.StringVar(value="Weekly")
        for frequency in ["Once a Month", "Once a Week", "Daily"]:
            tk.Radiobutton(self.container, text=frequency, variable=self.notification_frequency, value=frequency).pack(anchor='w')

        tk.Label(self.container, text="Reminders for favorited events:").pack(pady=5)
        self.reminder_frequency = tk.StringVar(value="Weekly")
        for reminder in ["Once a Month", "Once a Week", "Daily"]:
            tk.Radiobutton(self.container, text=reminder, variable=self.reminder_frequency, value=reminder).pack(anchor='w')

        button_frame = tk.Frame(self.container)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Skip", command=self.next_question).pack(side="left", padx=10)
        tk.Button(button_frame, text="Finish", command=self.save_notifications).pack(side="left", padx=10)

    def save_notifications(self):
        self.answers['price_tracking'] = bool(self.price_tracking_var.get())
        self.answers['notification_frequency'] = self.notification_frequency.get()
        self.answers['reminder_frequency'] = self.reminder_frequency.get()
        self.next_question()

    def next_question(self):
        self.current_question += 1
        self.show_question()

    def finish(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        tk.Label(self.container, text="Thank you for completing the questionnaire!").pack(pady=20)
        tk.Button(self.container, text="Exit", command=self.quit).pack(pady=10)
        print("Collected Answers:", self.answers)

if __name__ == "__main__":
    app = QuestionnaireApp()
    app.mainloop()

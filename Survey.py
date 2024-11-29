import tkinter as tk
from tkinter import messagebox
 
class QuestionnaireApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Event Preferences Questionnaire")
        self.master.geometry("390x934")  # Screen size for an iPhone
        self.current_question = 0
        self.answers = {}

        # Create a container frame
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

    # Question 1: Zip Code Question
    def zip_code_question(self):
        self.container.configure(bg="white")  # Set background color for the entire screen
        tk.Label(self.container, text="Questions Start Here", bg="white", fg="black", font=("Arial", 14, "bold")).pack(anchor="w", pady=(5, 0))

        # Question header
        tk.Label(self.container, text="Question 1/5", bg="#88c999", fg="white", font=("Arial", 16, "bold"), height=2).pack(fill="x")

        # Question text
        tk.Label(self.container, text="Preferred Zip Code", bg="white", fg="black", font=("Arial", 14, "bold")).pack(pady=(20, 10))
        tk.Label(self.container, text="Enter a 5-digit zip code", bg="white", fg="black", font=("Arial", 14, "bold")).pack(pady=5)

        # Input field
        self.zip_code_entry = tk.Entry(self.container, font=("Arial", 14), width=20, justify="center")
        self.zip_code_entry.insert(0, "")
        self.zip_code_entry.pack(pady=10)

        # Button frame
        button_frame = tk.Frame(self.container, bg="white")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Back", command=self.previous_question, bg="#88c999", fg="white", font=("Arial", 14, "bold"), width=10).pack(side="left", padx=10)
        tk.Button(button_frame, text="Next", command=self.save_zip_code, bg="#88c999", fg="white", font=("Arial", 14, "bold"), width=10).pack(side="left", padx=10)
        tk.Button(button_frame, text="Skip", command=self.next_question, bg="#88c999", fg="white", font=("Arial", 14, "bold"), width=10).pack(side="left", padx=10)

    def save_zip_code(self):
        zip_code = self.zip_code_entry.get()
        if zip_code.strip() == "":
            messagebox.showwarning("Input Required", "Please enter a valid 5-digit zip code or click Skip.")
        else:
            self.answers['zip_code'] = zip_code
            self.next_question()

    # Question 2: Event Type Question
    def event_type_question(self):
        tk.Label(self.container, text="Question 2/5", bg="#88c999", fg="white", font=("Arial", 16, "bold"), height=2).pack(fill="x")
        tk.Label(self.container, text="Select the types of events you like:", bg="white", fg="black", font=("Arial", 14, "bold")).pack(pady=10)

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
            tk.Checkbutton(self.container, text=event, variable=var, bg="white", font=("Arial", 14, "bold"), fg="black").pack(anchor='w')

        button_frame = tk.Frame(self.container, bg="white")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Skip", command=self.next_question, bg="#88c999", fg="white", font=("Arial", 14, "bold")).pack(side="left", padx=10)
        tk.Button(button_frame, text="Next", command=self.save_event_types, bg="#88c999", fg="white", font=("Arial", 14, "bold")).pack(side="left", padx=10)

    def save_event_types(self):
        selected_events = [event for event, var in self.event_vars.items() if var.get() == 1]
        self.answers['event_types'] = selected_events
        self.next_question()

    # Question 3: Music Genre Question
    def music_genre_question(self):
        tk.Label(self.container, text="Question 3/5", bg="#88c999", fg="white", font=("Arial", 16, "bold"), height=2).pack(fill="x")
        tk.Label(self.container, text="What music genres are you interested in?", bg="white", fg="black", font=("Arial", 14, "bold")).pack(pady=10)

        self.music_vars = {
            "Blues/Gospel": tk.IntVar(),
            "Classical": tk.IntVar(),
            "Country": tk.IntVar(),
            "Electronic/Techno": tk.IntVar(),
            "Hip Hop/Rap": tk.IntVar(),
            "Indie": tk.IntVar(),
            "Jazz": tk.IntVar(),
            "Latin": tk.IntVar(),
            "Pop": tk.IntVar(),
            "Rock and Roll": tk.IntVar()
        }

        for genre, var in self.music_vars.items():
            tk.Checkbutton(self.container, text=genre, variable=var, bg="white", font=("Arial", 14, "bold"), fg="black").pack(anchor='w')

        button_frame = tk.Frame(self.container, bg="white")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Skip", command=self.next_question, bg="#88c999", fg="white", font=("Arial", 14, "bold")).pack(side="left", padx=10)
        tk.Button(button_frame, text="Next", command=self.save_music_genres, bg="#88c999", fg="white", font=("Arial", 14, "bold")).pack(side="left", padx=10)

    def save_music_genres(self):
        selected_genres = [genre for genre, var in self.music_vars.items() if var.get() == 1]
        self.answers['music_genres'] = selected_genres
        self.next_question()

    # Question 4: Sports Interest Question
    def sports_interest_question(self):
        tk.Label(self.container, text="Question 4/5", bg="#88c999", fg="white", font=("Arial", 16, "bold"), height=2).pack(fill="x")
        tk.Label(self.container, text="What sports are you interested in?", bg="white", fg="black", font=("Arial", 14, "bold")).pack(pady=10)

        self.sports_vars = {
            "Soccer": tk.IntVar(),
            "Football": tk.IntVar(),
            "Tennis": tk.IntVar(),
            "Golf": tk.IntVar(),
            "Cricket": tk.IntVar(),
            "Wrestling": tk.IntVar(),
            "Martial Arts": tk.IntVar(),
            "Swimming": tk.IntVar(),
            "Volleyball": tk.IntVar(),
            "Esports": tk.IntVar()
        }

        for sport, var in self.sports_vars.items():
            tk.Checkbutton(self.container, text=sport, variable=var, bg="white", font=("Arial", 14, "bold"), fg="black").pack(anchor='w')

        button_frame = tk.Frame(self.container, bg="white")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Skip", command=self.next_question, bg="#88c999", fg="white", font=("Arial", 14, "bold")).pack(side="left", padx=10)
        tk.Button(button_frame, text="Next", command=self.save_sports_interests, bg="#88c999", fg="white", font=("Arial", 14, "bold")).pack(side="left", padx=10)

    def save_sports_interests(self):
        selected_sports = [sport for sport, var in self.sports_vars.items() if var.get() == 1]
        self.answers['sports_interests'] = selected_sports
        self.next_question()

    # Question 5: Notification Preferences Question
    def notification_preferences_question(self):
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

        tk.Button(button_frame, text="Skip", command=self.next_question, bg="#88c999", fg="white", font=("Arial", 14, "bold")).pack(side="left", padx=10)
        tk.Button(button_frame, text="Finish", command=self.save_notifications, bg="#88c999", fg="white", font=("Arial", 14, "bold")).pack(side="left", padx=10)

    def save_notifications(self):
        self.answers['price_tracking'] = bool(self.price_tracking_var.get())
        self.answers['notification_frequency'] = self.notification_frequency.get()
        self.answers['reminder_frequency'] = self.reminder_frequency.get()
        self.next_question()

    def previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.show_question()

    def next_question(self):
        self.current_question += 1
        self.show_question()


    def finish(self):
        for widget in self.container.winfo_children():
            widget.destroy()
        tk.Label(self.container, text="Thank you for completing the questionnaire!", bg="white", fg="black", font=("Arial", 16, "bold")).pack(pady=20)
        tk.Button(self.container, text="Exit", command=self.quit, bg="#88c999", fg="white", font=("Arial", 14, "bold")).pack(pady=10)
        print("Collected Answers:", self.answers)

if __name__ == "__main__":
    app = QuestionnaireApp()
    app.mainloop()

import tkinter as tk
from tkinter import messagebox

class QuestionnaireApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Event Preferences Questionnaire")
        self.geometry("400x300")
        self.current_question = 0
        self.answers = {}
        self.create_widgets()

    def create_widgets(self):
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.show_question()

    def show_question(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        if self.current_question == 0:
            self.zip_code_question()
        elif self.current_question == 1:
            self.event_type_question()
        # Add more elif blocks here for additional questions
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
        if not selected_events:
            messagebox.showwarning("Selection Required", "Please select at least one event type or click Skip.")
        else:
            self.answers['event_types'] = selected_events
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
        # You can add code here to process the collected answers further

if __name__ == "__main__":
    app = QuestionnaireApp()
    app.mainloop()

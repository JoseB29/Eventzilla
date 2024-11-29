import tkinter as tk

class MoodCheckScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()
 
    def create_widgets(self):
        # Title Bar
        title_frame = tk.Frame(self, bg="green")
        title_frame.pack(fill="x")

        tk.Label(
            title_frame,
            text="Mood Check",
            font=("Helvetica", 26, "bold"),
            fg="white",
            bg="green",
        ).pack(pady=8)

        # Subtitle
        tk.Label(
            self,
            text="How Are You Feeling Today?",
            font=("Helvetica", 14, "bold"),
            anchor="center",
        ).pack(pady=(10, 15))

        # Mood Options (Checkboxes with Descriptions)
        self.mood_options = {
            "Let's go out!": "Happy, Excited, Energized",
            "Home Sweet Home...": "Introverted, Relaxed, Tired",
            "Exploration Vibes :)": "Curious, Bored, Hopeful",
            "The Good Ol' Times": "Nostalgic, Reflective, Content, Hopeful",
            "Rage Bait": "Frustrated, Anxious",
            "Sad Core :(": "Sad, Miserable, Gloomy",
        }

        self.selected_moods = {}
        checkbox_frame = tk.Frame(self)
        checkbox_frame.pack(pady=8)

        for i, (mood, description) in enumerate(self.mood_options.items()):
            self.add_mood_checkbox(checkbox_frame, mood, description, row=i)

        # Done Button
        tk.Button(
            self,
            text="Done",
            command=self.submit_selection,
            bg="green",
            fg="white",
            font=("Helvetica", 16),
            width=8,
        ).pack(pady=18)

    def add_mood_checkbox(self, parent, mood, description, row):
        frame = tk.Frame(parent)
        frame.grid(row=row // 2, column=row % 2, padx=10, pady=10, sticky="w")

        var = tk.BooleanVar()
        self.selected_moods[mood] = var

        checkbox = tk.Checkbutton(
            frame,
            text=mood,
            variable=var,
            font=("Helvetica", 9),
            anchor="w",
        )
        checkbox.grid(row=0, column=0, sticky="w")


        tk.Label(
            frame,
            text=f"Moods: {description}",
            font=("Helvetica", 8),
            fg="gray",
            wraplength=200,
            justify="left",
        ).grid(row=1, column=0, sticky="w")

    def submit_selection(self):
        # Get the selected moods
        selected = [mood for mood, var in self.selected_moods.items() if var.get()]
        print(f"Selected Moods: {selected}")
        
        # Switch to the DiscoverPage after submission
        self.master.show_discover_page()
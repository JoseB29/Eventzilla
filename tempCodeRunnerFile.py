def show_mood_check_screen(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        self.current_screen = MoodCheck(self)
        self.current_screen.pack(fill="both", expand=True)
        print("Showing MoodCheck screen")
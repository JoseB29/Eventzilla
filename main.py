import tkinter as tk
from loginMenu import LoginApp
from createAccount import CreateAccount
from confirmEmail import ConfirmEmailScreen
from discoverPage import DiscoverPage
from moodCheck import MoodCheckScreen
from Survey import QuestionnaireApp
from searchPage import SearchPage
 
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EventZilla")
        self.current_screen = None
        self.show_screen1()

    # Function to show the login screen
    def show_screen1(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        self.current_screen = LoginApp(self)
        self.current_screen.pack(fill='both', expand=True)
        print("Showing LoginApp screen")

    # Function to show the discover page
    def show_screen2(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        #self.current_screen = DiscoverPage(self)
        self.current_screen = MoodCheckScreen(self)
        self.current_screen.pack(fill='both', expand=True)
        #print("Showing DiscoverPage screen")
        print("Showing MoodCheck screen")

    # Function to show the create account screen
    def show_screen3(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        self.current_screen = CreateAccount(self)
        self.current_screen.pack(fill='both', expand=True)
        print("Showing CreateAccount screen")

    # Function to show the confirm email screen
    def show_screen4(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        self.current_screen = ConfirmEmailScreen(self)
        self.current_screen.pack(fill='both', expand=True)
        print("Showing ConfirmEmailScreen screen")

    # Function to show the survey screen
    def show_screen5(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        self.current_screen = QuestionnaireApp(self)
        self.current_screen.pack(fill="both", expand=True)
        print("Showing Survey screen")
    
    # Function to show the mood check screen
    def show_mood_check_screen(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        self.current_screen = MoodCheckScreen(self)
        self.current_screen.pack(fill="both", expand=True)
        print("Showing MoodCheck screen")

    # Function to show the discover page
    def show_discover_page(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        self.current_screen = DiscoverPage(self)  
        self.current_screen.pack(fill="both", expand=True)
        print("Showing DiscoverPage screen")

    def show_search_page(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        self.current_screen = SearchPage(self)
        self.current_screen.pack(fill="both", expand=True)
        print("Showing SearchPage screen")

if __name__ == "__main__":
    app = App()
    app.mainloop()
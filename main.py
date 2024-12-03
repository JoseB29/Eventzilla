import tkinter as tk
from loginMenu import LoginApp
from createAccount import CreateAccount
from confirmEmail import ConfirmEmailScreen
from discoverPage import DiscoverPage
from moodCheck import MoodCheckScreen
from Survey import QuestionnaireApp
from searchPage import SearchPage
from myEventsPage import MyEventsPage
from profilePage import ProfilePage
from forYouPage import ForYouPage
from searchPageDef import DefSearchPage
from eventInfoPage import EventPageInfo
from eventInfoPageDiscoverAndForYou import EventPageInfoTwo
from Settings import SettingsScreen

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EventZilla")
        self.current_screen = None
        self.current_page = None  # Initialize current_page
        self.previous_page = None  # Initialize previous_page

        self.email = None

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

    # Function to show the settings screen
    def show_screen6(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        self.current_screen = SettingsScreen(self)
        self.current_screen.pack(fill="both", expand=True)
        print("Showing Settings screen")
    
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

    # Function to switch to the search page
    def switch_to_search_page(self, search_query):
    # Destroy the current page completely
        for widget in self.winfo_children():
            widget.destroy()

        # Add the SearchPage
        self.current_page = SearchPage(self, search_query)
        self.current_page.pack(fill="both", expand=True)

    # Function to switch to the default search page
    def switch_to_def_search_page(self):
        # Destroy the current page completely
        for widget in self.winfo_children():
            widget.destroy()

        # Create a new SearchPage instance (without relying on DefSearchPage)
        self.current_page = DefSearchPage(self)  # Pass the App instance
        self.current_page.pack(fill="both", expand=True)

    # Function to switch to the My Events page
    def switch_to_my_events_page(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.current_page = MyEventsPage(self)
        self.current_page.pack(fill="both", expand=True)

    # Function to switch to the Profile page
    def switch_to_profile_page(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.current_page = ProfilePage(self, email=self.email)
        self.current_page.pack(fill="both", expand=True)

    # Function to switch to the For You page
    def switch_to_for_you_page(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.current_page = ForYouPage(self)
        self.current_page.pack(fill="both", expand=True)

    # Function to switch to the event info page
    def switch_to_event_info_page(self,search_query, event):
        for widget in self.winfo_children():
            widget.destroy()

        self.current_page = EventPageInfo(self,search_query, event)
        self.current_page.pack(fill="both", expand=True)

    def switch_to_event_info_pageTwo(self, event):
        for widget in self.winfo_children():
            widget.destroy()

        self.current_page = EventPageInfoTwo(self, event)
        self.current_page.pack(fill="both", expand=True)

    

        


        


if __name__ == "__main__":
    app = App()
    app.mainloop()
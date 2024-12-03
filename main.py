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

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EventZilla")
        self.current_screen = None
        self.previous_screens = []  # Stack to track previous screens

        self.email = None  # Shared data attribute

        self.show_screen1()  # Start with the login screen

    def switch_screen(self, screen_class, *args, **kwargs):
        """
        Core method to switch screens.
        :param screen_class: Class of the screen to show.
        :param args: Positional arguments for screen initialization.
        :param kwargs: Keyword arguments for screen initialization.
        """
        if self.current_screen is not None:
            print(f"Destroying {self.current_screen.__class__.__name__} screen")
            self.previous_screens.append(self.current_screen)  # Save current screen
            self.current_screen.destroy()

        self.current_screen = screen_class(self, *args, **kwargs)
        self.current_screen.pack(fill="both", expand=True)
        print(f"Showing {screen_class.__name__} screen")

    def show_screen1(self):
        self.switch_screen(LoginApp)

    def show_screen2(self):
        self.switch_screen(MoodCheckScreen)

    def show_screen3(self):
        self.switch_screen(CreateAccount)

    def show_screen4(self):
        self.switch_screen(ConfirmEmailScreen)

    def show_screen5(self):
        self.switch_screen(QuestionnaireApp)

    def show_mood_check_screen(self):
        self.switch_screen(MoodCheckScreen)

    def show_discover_page(self):
        self.switch_screen(DiscoverPage)

    def switch_to_search_page(self, search_query):
        self.switch_screen(SearchPage, search_query)

    def switch_to_def_search_page(self):
        self.switch_screen(DefSearchPage)

    def switch_to_my_events_page(self):
        self.switch_screen(MyEventsPage)

    def switch_to_profile_page(self):
        self.switch_screen(ProfilePage, email=self.email)

    def switch_to_for_you_page(self):
        self.switch_screen(ForYouPage)

    def switch_to_event_info_page(self, event_id=None):
        self.switch_screen(EventPageInfo, event_id=event_id)

    def switch_to_previous_page(self):
        if self.previous_screens:
            print(f"Returning to previous screen: {self.previous_screens[-1].__class__.__name__}")
            self.current_screen.destroy()
            self.current_screen = self.previous_screens.pop()
            self.current_screen.pack(fill="both", expand=True)
        else:
            print("No previous screens. Returning to DiscoverPage.")
            self.show_discover_page()


if __name__ == "__main__":
    app = App()
    app.mainloop()

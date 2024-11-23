import tkinter as tk
from loginMenu import LoginApp
from createAccount import CreateAccount
from confirmEmail import ConfirmEmailScreen
from discoverPage import DicoverPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EventZilla")
        self.current_screen = None
        self.show_screen1()

    def show_screen1(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        self.current_screen = LoginApp(self)
        self.current_screen.pack(fill='both', expand=True)
        print("Showing LoginApp screen")

    def show_screen2(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        self.current_screen = DicoverPage(self)
        self.current_screen.pack(fill='both', expand=True)
        print("Showing DicoverPage screen")

    def show_screen3(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        self.current_screen = CreateAccount(self)
        self.current_screen.pack(fill='both', expand=True)
        print("Showing CreateAccount screen")

    def show_screen4(self):
        if self.current_screen is not None:
            print("Destroying current screen")
            self.current_screen.destroy()
        self.current_screen = ConfirmEmailScreen(self)
        self.current_screen.pack(fill='both', expand=True)
        print("Showing ConfirmEmailScreen screen")

if __name__ == "__main__":
    app = App()
    app.mainloop()
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
 
#create a class called DiscoverPage
class SearchPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Search")
        self.master.geometry("390x934")  # iPhone size




       
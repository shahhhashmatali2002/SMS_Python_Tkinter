from tkinter import *
import tkinter as tk
from tkinter import messagebox

class lobby:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x650+40+30')
        self.root.title("User Login")
        self.root.resizable('false', 'false')

if __name__ == '__main__':
    root = Tk()
    obj = lobby(root)
    root.mainloop()
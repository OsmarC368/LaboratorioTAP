import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class AbcView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Determinar Tipo ABC")
        self.window.geometry("800x500")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Menu Principal-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.pack(pady=8)

    def show(self):
        self.window.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class MenuView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Menu Principal")
        self.window.geometry("600x375")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Menu Principal-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.pack(pady=8)

        #Create Options
        self.createOptions()
        self.exitButton = tk.Button(
            self.window,
                text="Salir",
                width=25,
                height=2,
                command= lambda: self.close(),
                background="#243d55",
                activebackground="#61b9eb",
                foreground="#aaaaaa",
                activeforeground="WHITE",
                border=3,
                font=("Arial", 10, "bold")
        ).pack(pady=6)


    def show(self):
        self.window.deiconify()

    def initiate(self):
        self.window.mainloop()

    def showMessage(self, title, message):
        messagebox.showinfo(title, message,)

    def close(self):
        self.window.destroy()

    def createOptions(self):
        options = self.controller.options()
        for key, value in options.items():
            tk.Button(
                self.window,
                text=f"{value}",
                width=25,
                height=2,
                command= lambda k=key: self.controller.controlOptions(k),
                background="#243d55",
                activebackground="#61b9eb",
                foreground="#aaaaaa",
                activeforeground="WHITE",
                border=3,
                font=("Arial", 10, "bold")
            ).pack(pady=6)
    
    def hide(self):
        self.window.withdraw()
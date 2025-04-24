import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class datosABCView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("\-ABC Opciones-/")
        self.window.geometry("450x250")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-ABC Opciones-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.pack(pady=8)

        #Create Options
        self.defaultButton = tk.Button(
            self.window,
            text="Datos de Enunciado",
            width=25,
            height=2,
            command= lambda: self.controller.controlOptions("1"),
            background="#243d55",
            activebackground="#61b9eb",
            foreground="#aaaaaa",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
        ).pack(pady=6)

        self.userDataButton = tk.Button(
            self.window,
            text="Ingresar Vectores",
            width=25,
            height=2,
            command= lambda: self.controller.controlOptions("2"),
            background="#243d55",
            activebackground="#61b9eb",
            foreground="#aaaaaa",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
        ).pack(pady=6)


    def close(self):
        self.window.destroy()

    def initiate(self):
        self.window.mainloop()

    def showMessage(self, title, message):
        messagebox.showinfo(title, message,)


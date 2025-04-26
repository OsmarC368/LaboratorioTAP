import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class ModelsOptionsView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("\-Opciones de Modelos-/")
        self.window.geometry("450x350")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Opciones de Modelos-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.pack(pady=8)

        #Create Options
        self.loteEcoButton = tk.Button(
            self.window,
            text="Lote Econmico",
            width=25,
            height=2,
            command= lambda: self.controller.Standard(),
            background="#243d55",
            activebackground="#61b9eb",
            foreground="#aaaaaa",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
        ).pack(pady=6)

        self.loteProbButton = tk.Button(
            self.window,
            text="Probabilistico",
            width=25,
            height=2,
            command= lambda: self.controller.Probabilistic(),
            background="#243d55",
            activebackground="#61b9eb",
            foreground="#aaaaaa",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
        ).pack(pady=6)
        
        self.loteDescButton = tk.Button(
            self.window,
            text="Descuento",
            width=25,
            height=2,
            #command= lambda: self.controller.controlOptions("2"),
            background="#243d55",
            activebackground="#61b9eb",
            foreground="#aaaaaa",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
        ).pack(pady=6)

        self.menuButton = tk.Button(
            self.window,
            text="Menu Principal",
            width=25,
            height=2,
            command= lambda: self.controller.mainMenu(),
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
        
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

dataDefault = [["a", 80, 522],
               ["b", 514, 54.07],
               ["c", 19, 0.65],
               ["d", 2442, 16.11],
               ["e", 650, 4.61],
               ["f", 128, 0.63],
               ["g", 2500, 1.2],
               ["h", 4, 22.05],
               ["i", 25, 5.01],
               ["j", 2232, 2.48],
               ["k", 2, 4.78],
               ["l", 1, 38.03],
               ["m", , ],
               ["n", , ],
               ["o", , ],
               ["p", , ],
               ["q", , ],
               ["r", , ],
               ["s", , ],
               ]

class AbcView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Determinar Tipo ABC")
        self.window.geometry("800x500")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Determinar Tipo ABC-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.pack(pady=8)

        #TreeView
        self.tabla = ttk.Treeview()

    def show(self):
        self.window.mainloop()
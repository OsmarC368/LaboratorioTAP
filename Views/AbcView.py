import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class AbcView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Determinar Tipo ABC")
        self.window.geometry("800x600")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Determinar Tipo ABC-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.pack(pady=8)

        #TreeView
        self.tabla = ttk.Treeview(self.window, columns=("col1","col2", "col3", "col4"), height=20)
        self.tabla.column("#0", width=120)
        self.tabla.column("col1", width=120, anchor=tk.CENTER)
        self.tabla.column("col2", width=120, anchor=tk.CENTER)
        self.tabla.column("col3", width=120, anchor=tk.CENTER)
        self.tabla.column("col4", width=120, anchor=tk.CENTER)
        self.tabla.heading("#0", text="Producto", anchor=tk.CENTER)
        self.tabla.heading("col1", text="Uso Anual", anchor=tk.CENTER)
        self.tabla.heading("col2", text="Costo Unitario", anchor=tk.CENTER)
        self.tabla.heading("col3", text="Valor Total", anchor=tk.CENTER)
        self.tabla.heading("col4", text="Tipo", anchor=tk.CENTER)
        self.tabla.pack()
        self.loadTable()

        self.buttonGraph = tk.Button(
            self.window, 
            command=self.controller.showPieGraph, 
            text="Grafico",
            background="#243d55",
            activebackground="#61b9eb",
            foreground="#aaaaaa",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
            ).pack(pady=5)
        
        self.buttonMenu = tk.Button(
            self.window, 
            command=self.controller.showMenu, 
            text="Menu Principal",
            background="#243d55",
            activebackground="#61b9eb",
            foreground="#aaaaaa",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
            ).pack(pady=5)

        
    def show(self):
        self.window.mainloop()

    def close(self):
        self.window.destroy()

    def showMessage(self, title, message):
        messagebox.showinfo(title, message)

    def loadTable(self):
        data = self.controller.getDataABC()
        for x in data:
            self.tabla.insert("", tk.END, text=f"{x[0]}", values=(x[1], x[2], x[3], x[4]))
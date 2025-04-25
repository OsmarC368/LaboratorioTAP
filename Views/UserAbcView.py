import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class UserAbcView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Ingresar Datos para los Vectores")
        self.window.geometry("500x540")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Ingresar Parametros para los Vectores-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.pack(pady=6)

        #Variables
        self.vectores = tk.StringVar()
        self.numeroProductos = tk.StringVar()
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()

        #labels and Entrys
        self.labelNumeroProductos = tk.Label(self.window, text="Ingrese el Numero de Productos", foreground="White", font=("Arial", 12, "bold"), background="#2b2f36")
        self.labelNumeroProductos.pack(pady=6)

        self.entryNumeroProductos = tk.Entry(self.window, textvariable=self.numeroProductos, width=40)
        self.entryNumeroProductos.pack(pady=6)

        self.labelVar1 = tk.Label(self.window, text="Ingrese el limite inferior del Uso Anual Producto", foreground="White", font=("Arial", 12, "bold"), background="#2b2f36")
        self.labelVar1.pack(pady=6)

        self.entryVar1 = tk.Entry(self.window, textvariable=self.var1, width=40)
        self.entryVar1.pack(pady=6)

        self.labelVar2 = tk.Label(self.window, text="Ingrese el limite superior del Uso Anual Producto", foreground="White", font=("Arial", 12, "bold"), background="#2b2f36")
        self.labelVar2.pack(pady=6)

        self.entryVar2 = tk.Entry(self.window, width=40)
        self.entryVar2.pack(pady=6)

        self.labelVar3 = tk.Label(self.window, text="Ingrese el limite inferior del Costo Unitario del Producto", foreground="White", font=("Arial", 12, "bold"), background="#2b2f36")
        self.labelVar3.pack(pady=6)

        self.entryVar3 = tk.Entry(self.window, width=40)
        self.entryVar3.pack(pady=6)

        self.labelVar4 = tk.Label(self.window, text="Ingrese el limite superior del Costo Unitario del Producto", foreground="White", font=("Arial", 12, "bold"), background="#2b2f36")
        self.labelVar4.pack(pady=6)

        self.entryVar4 = tk.Entry(self.window, width=40)
        self.entryVar4.pack(pady=6)


        self.buttonCalc = tk.Button(
            self.window, 
            text="Calcular",
            width=25,
            height=2,
            command= lambda: self.controller.solveABC(),
            background="#243d55",
            activebackground="#61b9eb",
            foreground="WHITE",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
            ).pack(pady=10)
        
        self.buttonMenu = tk.Button(
            self.window,
            text="Menu Principal",
            width=25,
            height=2,
            command= lambda: self.controller.showMenu(),
            background="#243d55",
            activebackground="#61b9eb",
            foreground="WHITE",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
            ).pack(pady=10)


    def close(self):
        self.window.destroy()

    def initiate(self):
        self.window.mainloop()

    def showMessage(self, title, message):
        messagebox.showinfo(title, message,)
    
    def hide(self):
        self.window.withdraw()

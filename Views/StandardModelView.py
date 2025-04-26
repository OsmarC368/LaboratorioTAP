import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class StandardModelView:
    def __init__(self, controller):
        self.controller = controller
        self.x = 60
        self.window = tk.Tk()
        self.window.title("Lote Estandar")
        self.window.geometry("550x740")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Modelo de Lote Estandar-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.place(x=140, y=60)

        #labels and Entrys
        #Valor unitario
        self.labelC = tk.Label(self.window, text="Ingrese el valor unitario del Producto (c):", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelC.place(x=self.x, y=130)
        self.entryC = tk.Entry(self.window, width=20)
        self.entryC.place(x=self.x*6.1, y=130)
        
        #Valor de la Demanda
        self.labelD = tk.Label(self.window, text="Ingrese el valor de la Demanda (D):", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelD.place(x=self.x, y=170)
        self.entryD = tk.Entry(self.window, width=20)
        self.entryD.place(x=self.x*5.4, y=170)
        
        
        #Costo por Pedido
        self.labelK = tk.Label(self.window, text="Ingrese el valor del Costo por Pedido (k):", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelK.place(x=self.x, y=210)
        self.entryK = tk.Entry(self.window, width=20)
        self.entryK.place(x=self.x*6.05, y=210)
        
        
        #Costo de Almacenar
        self.labelH = tk.Label(self.window, text="Ingrese el costo de Almacenar (h):", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelH.place(x=self.x, y=250)
        self.entryH = tk.Entry(self.window, width=20)
        self.entryH.place(x=self.x*5.25, y=250)

        
        #Tiempo de Entrega
        self.labelL = tk.Label(self.window, text="Ingrese el Tiempo de Entrega (l):", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelL.place(x=self.x, y=290)
        self.entryL = tk.Entry(self.window, width=20)
        self.entryL.place(x=self.x*5.15, y=290)
        
        
        #Costo por Perdida
        self.labelPer = tk.Label(self.window, text="Ingrese el Costo por Perdida: \nEn caso de que tenga", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelPer.place(x=self.x, y=330)
        self.entryPer = tk.Entry(self.window, width=20)
        self.entryPer.place(x=self.x*5, y=330)

        #Resultado TEXT
        self.labelResult = tk.Label(self.window, text="Resultado", font=("Arial", 13, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelResult.place(x=230, y=450)
        self.textResult = tk.Text(self.window, height=10, width=50)
        self.textResult.place(x=75, y=480)


        self.buttonCalc = tk.Button(
            self.window, 
            text="Calcular",
            width=20,
            height=1,
            command= lambda: self.controller.solve(),
            background="#243d55",
            activebackground="#61b9eb",
            foreground="WHITE",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
            ).place(x=self.x, y=390)
        
        self.buttonGraph = tk.Button(
            self.window, 
            text="Grafico",
            width=20,
            height=1,
            command= lambda: self.controller.showGraph(),
            background="#243d55",
            activebackground="#61b9eb",
            foreground="WHITE",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold"),
            state="disabled"
            )
        
        self.buttonGraph.place(x=self.x*5, y=390)
        
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
            ).place(x=170, y=670)


    def close(self):
        self.window.destroy()

    def initiate(self):
        self.window.mainloop()

    def showMessage(self, title, message):
        messagebox.showinfo(title, message,)
    
    def hide(self):
        self.window.withdraw()
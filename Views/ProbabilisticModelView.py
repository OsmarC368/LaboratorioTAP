import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class ProbabilisticModelView:
    def __init__(self, controller):
        self.controller = controller
        self.x = 60
        self.window = tk.Tk()
        self.window.title("Probabilistico")
        self.window.geometry("590x840")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Modelo Probabilistico-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.place(x=190, y=60)

        #labels and Entrys
        #Costo por Pedido
        self.labelK = tk.Label(self.window, text="Ingrese el valor del Costo por Pedido (k):", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelK.place(x=self.x, y=130)
        self.entryK = tk.Entry(self.window, width=20)
        self.entryK.place(x=self.x*6.05, y=130)

        #Costo de Almacenar
        self.labelH = tk.Label(self.window, text="Ingrese el costo de Almacenar (h):", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelH.place(x=self.x, y=170)
        self.entryH = tk.Entry(self.window, width=20)
        self.entryH.place(x=self.x*5.25, y=170)

        #Valor por Producto Acumulado
        self.labelPa = tk.Label(self.window, text="Ingrese el valor de Costo Producto Acumulado(pA):", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelPa.place(x=self.x, y=210)
        self.entryPa = tk.Entry(self.window, width=20)
        self.entryPa.place(x=self.x*7.4, y=210)
        
        #Valor Promedio
        self.labelU = tk.Label(self.window, text="Ingrese el valor Promedio (u):", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelU.place(x=self.x, y=250)
        self.entryU = tk.Entry(self.window, width=20)
        self.entryU.place(x=self.x*4.8, y=250)
        
        #Dias Laborales
        self.labeldLab = tk.Label(self.window, text="Ingrese el numero de Dias Laborales:", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labeldLab.place(x=self.x, y=290)
        self.entrydLab = tk.Entry(self.window, width=20)
        self.entrydLab.place(x=self.x*5.65, y=290)
        
        #Desviacion
        self.labelDes = tk.Label(self.window, text="Ingrese el valor de la Desviacion (des):", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelDes.place(x=self.x, y=330)
        self.entryDes = tk.Entry(self.window, width=20)
        self.entryDes.place(x=self.x*5.9, y=330)

        #Producto Acumulado Perdido
        self.labelPaPerdida = tk.Label(self.window, text="Ingrese el valor unitario de la Perdida (pAPerdida):\nen caso de no tener ingrese 0", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelPaPerdida.place(x=self.x, y=370)
        self.entryPaPerdida = tk.Entry(self.window, width=20)
        self.entryPaPerdida.place(x=self.x*7.3, y=370)

        #Resultado TEXT
        self.labelResult = tk.Label(self.window, text="Resultado", font=("Arial", 13, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelResult.place(x=255, y=490)
        self.textResult = tk.Text(self.window, height=10, width=50)
        self.textResult.place(x=95, y=520)


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
            ).place(x=self.x, y=425)
        
        self.buttonGraph = tk.Button(
            self.window, 
            text="Grafico",
            width=20,
            height=1,
            #command= lambda: self.controller.showGraph(),
            background="#243d55",
            activebackground="#61b9eb",
            foreground="WHITE",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold"),
            state="disabled"
            )
        
        self.buttonGraph.place(x=self.x*6.1, y=425)
        
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
            ).place(x=190, y=710)


    def close(self):
        self.window.destroy()

    def initiate(self):
        self.window.mainloop()

    def showMessage(self, title, message):
        messagebox.showinfo(title, message,)
    
    def hide(self):
        self.window.withdraw()
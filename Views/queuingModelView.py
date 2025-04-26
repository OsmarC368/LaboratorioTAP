import tkinter as tk
from tkinter import messagebox

class queuingModelView:
    def __init__(self, controller):
        self.controller = controller
        self.x = 55
        self.window = tk.Tk()
        self.window.title("Modelo de Cola")
        self.window.geometry("530x650")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Modelo de Cola M/M/1-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.place(x=160, y=60)

        #labels and Entrys
        #Tasa de Llegada
        self.labelLlegada = tk.Label(self.window, text="Ingrese la Tasa de Llegada:", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelLlegada.place(x=self.x, y=130)
        self.entryLlegada = tk.Entry(self.window, width=20)
        self.entryLlegada.place(x=self.x*4.9, y=130)

        #Tasa de Servicio
        self.labelServicio = tk.Label(self.window, text="Ingrese la tasa de Servicio:", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelServicio.place(x=self.x, y=170)
        self.entryServicio = tk.Entry(self.window, width=20)
        self.entryServicio.place(x=self.x*4.9, y=170)

        self.labelN = tk.Label(self.window, text="Ingrese el Nunero N:", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelN.place(x=self.x, y=210)
        self.entryN = tk.Entry(self.window, width=20)
        self.entryN.place(x=self.x*4.9, y=210)

        self.labelHora = tk.Label(self.window, text="Ingrese el Tiempo:", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelHora.place(x=self.x, y=250)
        self.entryHora = tk.Entry(self.window, width=20)
        self.entryHora.place(x=self.x*4.9, y=250)

        self.labelCSistema = tk.Label(self.window, text="Ingrese el Numero de Clientes en Sistema :", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelCSistema.place(x=self.x, y=290)
        self.entryCSistema = tk.Entry(self.window, width=20)
        self.entryCSistema.place(x=self.x*6.7, y=290)

        #Resultado TEXT
        self.labelResult = tk.Label(self.window, text="Resultado", font=("Arial", 13, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelResult.place(x=225, y=370)
        self.textResult = tk.Text(self.window, height=10, width=50)
        self.textResult.place(x=65, y=400)


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
            ).place(x=self.x, y=325)
        
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
        
        self.buttonGraph.place(x=self.x*6.1, y=325)
        
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
            ).place(x=170, y=580)


    def close(self):
        self.window.destroy()

    def initiate(self):
        self.window.mainloop()

    def showMessage(self, title, message):
        messagebox.showinfo(title, message,)
    
    def hide(self):
        self.window.withdraw()
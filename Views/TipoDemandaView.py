import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class TipoDemandaView:
    def __init__(self, controller):
        self.controller = controller
        self.x = 60
        self.window = tk.Tk()
        self.window.title("Tipo de Demanda")
        self.window.geometry("520x450")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Tipo de Demanda-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.place(x=170, y=60)

        #labels and Entrys
        #Arreglo de Datos
        self.labelData = tk.Label(self.window, text="Ingrese los Datos Separados por una coma (1,2,3,.....) ", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelData.place(x=self.x, y=130)
        self.entryData = tk.Entry(self.window, width=40)
        self.entryData.place(x=self.x*2.35, y=160)
        

        #Resultado TEXT
        self.labelResult = tk.Label(self.window, text="Resultado", font=("Arial", 13, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelResult.place(x=230, y=245)
        self.textResult = tk.Text(self.window, height=3, width=50)
        self.textResult.place(x=65, y=290)


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
            ).place(x=self.x, y=190)
        
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
            font=("Arial", 10, "bold")
            #state="disabled"
            )
        
        self.buttonGraph.place(x=self.x*5, y=190)

        
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
            ).place(x=170, y=380)


    def close(self):
        self.window.destroy()

    def initiate(self):
        self.window.mainloop()

    def showMessage(self, title, message):
        messagebox.showinfo(title, message,)
    

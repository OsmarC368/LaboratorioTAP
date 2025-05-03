import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Ejercicio2View:
    def __init__(self, controller):
        self.controller = controller
        self.x = 60
        self.window = tk.Tk()
        self.window.title("Ejercicio 2")
        self.window.geometry("590x750")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Ejercicio 2-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.place(x=230, y=60)

        #labels and Entrys

        self.labelCostoPedido = tk.Label(self.window, text="Costo de Pedido (k):", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelCostoPedido.place(x=self.x, y=130)
        self.entryCostoPedido = tk.Entry(self.window, width=20)
        self.entryCostoPedido.place(x=self.x*3.7, y=130)

        self.labelCostoAlmac = tk.Label(self.window, text="Costo de Almacenamiento (h):  ", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelCostoAlmac.place(x=self.x, y=170)
        self.entryCostoAlmac = tk.Entry(self.window, width=20)
        self.entryCostoAlmac.place(x=self.x*4.75, y=170)

        self.labelTiempoEntrega = tk.Label(self.window, text="Ingrese el Tiempo de Entrega:", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTiempoEntrega.place(x=self.x, y=210)
        self.entryTiempoEntrega = tk.Entry(self.window, width=20)
        self.entryTiempoEntrega.place(x=self.x*5, y=210)
        
        self.labelDemanda1 = tk.Label(self.window, text="Demanda Anual 1: ", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelDemanda1.place(x=self.x, y=250)
        self.entryDemanda1 = tk.Entry(self.window, width=40)
        self.entryDemanda1.place(x=self.x*3.5, y=250)
        
        self.labelDemanda2 = tk.Label(self.window, text="Demanda Anual 2: ", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelDemanda2.place(x=self.x, y=290)
        self.entryDemanda2 = tk.Entry(self.window, width=40)
        self.entryDemanda2.place(x=self.x*3.5, y=290)
        

        #Resultado TEXT
        self.labelResult = tk.Label(self.window, text="Resultado", font=("Arial", 13, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelResult.place(x=255, y=400)
        self.textResult = tk.Text(self.window, height=14, width=50)
        self.textResult.place(x=95, y=440)


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
            ).place(x=self.x, y=350)
        

        
        
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
            ).place(x=190, y=680)


    def close(self):
        self.window.destroy()

    def initiate(self):
        self.window.mainloop()

    def showMessage(self, title, message):
        messagebox.showinfo(title, message)
    
    def hide(self):
        self.window.withdraw()

    def add(self):
        if (self.entryInter.get() == "" or self.entryDesc.get() == "" or self.entryCostoAlm.get() == "" or self.entryCostoPrep.get() == ""):
            self.showMessage("ERROR", "Debe LLenar Todos los Campos")
        else:
            self.tabla.insert("", tk.END, text=f"{self.entryInter.get()}", values=(self.entryDesc.get(), 
                                                                               self.entryCostoAlm.get(), 
                                                                               self.entryCostoPrep.get()))
            self.controller.add()

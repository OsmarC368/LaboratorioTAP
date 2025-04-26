import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class discountModelView:
    def __init__(self, controller):
        self.controller = controller
        self.x = 60
        self.window = tk.Tk()
        self.window.title("Descuento")
        self.window.geometry("590x900")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Modelo de Descuento-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.place(x=180, y=60)

        #labels and Entrys

        self.labelInter = tk.Label(self.window, text="Ingrese el Intervalo de Unidades (1-5):", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelInter.place(x=self.x, y=130)
        self.entryInter = tk.Entry(self.window, width=20)
        self.entryInter.place(x=self.x*6, y=130)

        self.labelDesc = tk.Label(self.window, text="Ingrese el Valor del Descuento(%):", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelDesc.place(x=self.x, y=170)
        self.entryDesc = tk.Entry(self.window, width=20)
        self.entryDesc.place(x=self.x*5.6, y=170)

        self.labelCostoAlm = tk.Label(self.window, text="Ingrese el Costo de Almacenamiento:", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelCostoAlm.place(x=self.x, y=210)
        self.entryCostoAlm = tk.Entry(self.window, width=20)
        self.entryCostoAlm.place(x=self.x*6, y=210)
        
        self.labelCostoPrep = tk.Label(self.window, text="Ingrese el Costo de Preparacion:", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelCostoPrep.place(x=self.x, y=250)
        self.entryCostoPrep = tk.Entry(self.window, width=20)
        self.entryCostoPrep.place(x=self.x*5.3, y=250)
        
        self.labeldCant = tk.Label(self.window, text="Ingrese la Cantidad a Evaluar:", font=("Arial", 11, "bold"), foreground="WHITE", background="#2b2f36")
        self.labeldCant.place(x=self.x, y=500)
        self.entrydCant = tk.Entry(self.window, width=20)
        self.entrydCant.place(x=self.x*5.65, y=500)

        self.tabla = ttk.Treeview(self.window, columns=("col1","col2", "col3"), height=6)
        self.tabla.column("#0", width=115)
        self.tabla.column("col1", width=115, anchor=tk.CENTER)
        self.tabla.column("col2", width=115, anchor=tk.CENTER)
        self.tabla.column("col3", width=115, anchor=tk.CENTER)
        self.tabla.heading("#0", text="Unidades", anchor=tk.CENTER)
        self.tabla.heading("col1", text="Descuento", anchor=tk.CENTER)
        self.tabla.heading("col2", text="Costo de Almacenamiento", anchor=tk.CENTER)
        self.tabla.heading("col3", text="Costo de Preparacion", anchor=tk.CENTER)
        self.tabla.place(x=self.x, y=335)
        

        #Resultado TEXT
        self.labelResult = tk.Label(self.window, text="Resultado", font=("Arial", 13, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelResult.place(x=255, y=560)
        self.textResult = tk.Text(self.window, height=10, width=50)
        self.textResult.place(x=95, y=590)


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
            ).place(x=self.x, y=530)
        
        self.buttonAdd = tk.Button(
            self.window, 
            text="Añadir",
            width=20,
            height=1,
            command= lambda: self.add(),
            background="#243d55",
            activebackground="#61b9eb",
            foreground="WHITE",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
            ).place(x=self.x, y=290)
        
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
        
        self.buttonGraph.place()
        
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
            ).place(x=190, y=800)


    def close(self):
        self.window.destroy()

    def initiate(self):
        self.window.mainloop()

    def showMessage(self, title, message):
        messagebox.showinfo(title, message,)
    
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

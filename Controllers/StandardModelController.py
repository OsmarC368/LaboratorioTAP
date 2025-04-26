from Models.Models import Models
from Views.StandardModelView import StandardModelView
import matplotlib.pyplot as plt

class StandardModelController:
    def __init__(self, menuController):
        self.view = StandardModelView(self)
        self.menuController = menuController
        self.Q = 0
        self.D = 0
        self.c = 0
        self.h = 0
        self.k = 0
        self.e = 0
        self.pe = 0
    
    def close(self):
        self.view.close()

    def initiate(self):
        self.view.initiate()

    def solve(self):
        try:
            c = float(self.view.entryC.get())
            D = float(self.view.entryD.get())
            k = float(self.view.entryK.get())
            h = float(self.view.entryH.get())
            l = float(self.view.entryL.get())
            pe = float(self.view.entryPer.get())

            result = Models().simpleModel(c, D, k, h, l, pe)

            self.view.textResult.delete('1.0', "end")
            
            for i,x in enumerate(result[0]):
                self.view.textResult.insert('end', f"{x}\n")

            self.view.buttonGraph.config(state="normal")
            self.Q = result[1]
            self.D = result[2]
            self.c = result[3]
            self.h = result[4]
            self.k = result[5]
            self.e = result[6]
            self.pe = result[7]

        except:
            self.view.showMessage("ERROR", "Error en la Entrada de Datos")

    def showGraph(self):
        try:
            x = [(self.Q / 2)+i for i in range(50)]
            if self.pe == 0:
                y = [Models().calcCosto(self.D, self.c, (self.Q /2)+i, self.h, self.k) for i in range(50)]
            else:
                y = [Models().calcCostoFaltante(self.D, self.c, (self.Q /2)+i, self.h, self.k, e=self.e, pe=self.pe) for i in range(50)]

            plt.plot(x, y)
            plt.axvline(self.Q, color="green", linestyle="--")
            plt.title("Grafico de Cantidad x Costo", loc="center", fontsize=16)
            plt.legend(["Costo", "Valor de Q"])
            plt.xlabel("Cantidad")
            plt.ylabel("Costo")
            plt.show()
        except:
            self.view.showMessage("ERROR", "Error en la Creacion del Grafico")

    def showMenu(self):
        self.view.close()
        self.menuController.show()
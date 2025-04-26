import matplotlib.pyplot as plt
from Models.Models import Models
from Views.discountModelView import discountModelView


class discountModelController:
    def __init__(self, menuController):
        self.view = discountModelView(self)
        self.menuController = menuController
        self.discList = []
    
    def close(self):
        self.view.close()

    def initiate(self):
        self.view.initiate()


    def solve(self):
        try:
            dCant = float(self.view.entrydCant.get())

            result = Models().descModel(self.discList, dCant)

            self.view.textResult.delete('1.0', "end")
            
            for i,x in enumerate(result[0]):
                self.view.textResult.insert('end', f"{x}\n")

            "self.view.buttonGraph.config(state="normal")

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
            plt.title("Grafico de Costo", loc="center", fontsize=16)
            plt.legend(["Costo", "Valor de Q"])
            plt.show()
        except:
            self.view.showMessage("ERROR", "Error en la Creacion del Grafico")

    def add(self):
        self.discList.append([
            self.view.entryInter.get().split("-"),
            float(self.view.entryDesc.get()),
            float(self.view.entryCostoAlm.get()),
            float(self.view.entryCostoPrep.get())
        ])


    def showMenu(self):
        self.view.close()
        self.menuController.show()
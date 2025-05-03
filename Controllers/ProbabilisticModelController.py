import matplotlib.pyplot as plt
from Models.Models import Models
from Views.ProbabilisticModelView import ProbabilisticModelView


class ProbabilisticModelController:
    def __init__(self, menuController):
        self.view = ProbabilisticModelView(self)
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
            k = float(self.view.entryK.get())
            h = float(self.view.entryH.get())
            pA = float(self.view.entryPa.get())
            u = float(self.view.entryU.get())
            dLab = float(self.view.entrydLab.get())
            des = float(self.view.entryDes.get())
            pAPerdida = float(self.view.entryPaPerdida.get())

            result = Models().probModel(k, h, pA, u, dLab, des, pAPerdida)

            self.view.textResult.delete('1.0', "end")
            
            for i,x in enumerate(result[0]):
                self.view.textResult.insert('end', f"{x}\n")


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

    def showMenu(self):
        self.view.close()
        self.menuController.show()
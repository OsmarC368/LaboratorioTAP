from Views.AbcView import AbcView
from Models.Models import Models
import matplotlib.pyplot as plt

class AbcController:
    def __init__(self, menuController, data):
        self.view = AbcView(self)
        self.menuController = menuController
        self.data = data

    def show(self):
        self.view.show()

    def getDataABC(self):
        return Models().ABC(self.data)
    
    def showPieGraph(self):
        datos = self.getDataABC()
        y = [len([x for x in datos if x[1] == 'A']), len([x for x in datos if x[1] == "B"]), len([x for x in datos if x[1] == "C"])]
        labels = ["A", "B", "C"]
        plt.pie(y, labels=labels, autopct="%1.1f%%")
        plt.legend(title = "Tipo ABC")
        plt.title("Grafico de Torta |ABC|", loc="center", fontsize=16, color="blue")
        plt.show()

    def showMenu(self):
        self.view.close()
        self.menuController.show()
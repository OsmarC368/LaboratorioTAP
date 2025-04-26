from Models.Models import Models
from Views.queuingModelView import queuingModelView
import matplotlib.pyplot as plt

class queuingModelController:
    def __init__(self, menuController):
        self.view = queuingModelView(self)
        self.menuController = menuController
        self.p = 0

    
    def close(self):
        self.view.close()

    def initiate(self):
        self.view.initiate()

    def solve(self):
        try:
            llegada = float(self.view.entryLlegada.get())
            servicio = float(self.view.entryServicio.get())
            n = int(self.view.entryN.get())
            tiempo = float(self.view.entryHora.get())
            clientesN = float(self.view.entryCSistema.get())

            result = Models().queuingModel(llegada, servicio, n, tiempo, clientesN)
            self.view.textResult.delete('1.0', "end")
      
            for i,x in enumerate(result[0]):
                self.view.textResult.insert('end', f"{x}\n")
            self.view.buttonGraph.config(state="normal")
            self.p = result[1]
            
        except:
           self.view.showMessage("ERROR", "Error en la Entrada de Datos")
        

    def showGraph(self):
        try:
            x = [i for i in range(50)]
            y = [Models().probN(self.p, i) for i in range(50)]

            plt.plot(x, y)
            plt.title("Grafico de Colas", loc="center", fontsize=16)
            plt.xlabel("Valor de N")
            plt.ylabel("Prob de N")
            plt.show()
        except:
            self.view.showMessage("ERROR", "Error en la Creacion del Grafico")
        pass

    def showMenu(self):
        self.view.close()
        self.menuController.show()
import matplotlib.pyplot as plt
from Models.Models import Models
from Views.Ejercicio2View import Ejercicio2View
from Views.discountModelView import discountModelView


class Ejercicio2Controller:
    def __init__(self, menuController):
        self.view = Ejercicio2View(self)
        self.menuController = menuController

    
    def close(self):
        self.view.close()

    def initiate(self):
        self.view.initiate()


    def solve(self):
        try:
            demanda1 = list(map(lambda x: int(x), self.view.entryDemanda1.get().split(",")))
            demanda2 = list(map(lambda x: int(x), self.view.entryDemanda2.get().split(",")))
            h = float(self.view.entryCostoAlmac.get()) 
            k = float(self.view.entryCostoPedido.get())
            l = float(self.view.entryTiempoEntrega.get())

            result = Models().Ejercicio2(demanda1, demanda2, h, k, l)

            self.view.textResult.delete('1.0', "end")
      
            for i,x in enumerate(result):
                self.view.textResult.insert('end', f"{x}\n")


        except:
            self.view.showMessage("ERROR", "Error en la Entrada de Datos")



    def showMenu(self):
        self.view.close()
        self.menuController.show()
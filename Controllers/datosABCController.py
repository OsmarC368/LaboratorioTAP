from Views.datosABCView import datosABCView
from Controllers.AbcController import AbcController

dataDefault = [["a", 80, 522],
               ["b", 514, 54.07],
               ["c", 19, 0.65],
               ["d", 2442, 16.11],
               ["e", 650, 4.61],
               ["f", 128, 0.63],
               ["g", 2500, 1.2],
               ["h", 4, 22.05],
               ["i", 25, 5.01],
               ["j", 2232, 2.48],
               ["k", 2, 4.78],
               ["l", 1, 38.03],
               ["m", 6, 9.01],
               ["n", 12, 25.89],
               ["o", 101, 59.5],
               ["p", 715, 20.78],
               ["q", 1, 2.93],
               ["r", 35, 1],
               ["s", 1, 28.88]
               ]

class datosABCController:
    def __init__(self, menuController):
        self.view = datosABCView(self)
        self.menuController = menuController
    
    def close(self):
        self.view.close()

    def initiate(self):
        self.view.initiate()

    def controlOptions(self, opt):
        if opt == "1":
            self.view.close()
            AbcController(self.menuController, data=dataDefault).show()
        elif opt == "2":
            self.view.showMessage("Opcion","Opcion 2")
from Controllers.ModelsOptionsController import ModelsOptionsController
from Controllers.datosABCController import datosABCController
from Controllers.queuingModelController import queuingModelController
from Views.MenuView import MenuView


class MenuController:
    def __init__(self):
        self.view = MenuView(self)

    def options(self):
        return {
            "1": "Determinar Tipo ABC",
            "2": "Modelos de Inventario",
            "3": "Modelo de Colas",
        }
    
    def show(self):
        self.view.show()

    def initiate(self):
        self.view.initiate()

    def controlOptions(self, opt):
        if opt == "1":
            self.view.hide()
            datosABCController(self).initiate()
        elif opt == "2":
            self.view.hide()
            ModelsOptionsController(self).initiate()
        elif opt == "3":
            self.view.hide()
            queuingModelController(self).initiate()
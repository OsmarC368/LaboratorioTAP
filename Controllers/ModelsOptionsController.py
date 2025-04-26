
from Controllers.ProbabilisticModelController import ProbabilisticModelController
from Controllers.StandardModelController import StandardModelController
from Controllers.discountModelController import discountModelController
from Views.ModelsOptionsView import ModelsOptionsView


class ModelsOptionsController:
    def __init__(self, menuController):
        self.view = ModelsOptionsView(self)
        self.menuController = menuController
    
    def close(self):
        self.view.close()

    def initiate(self):
        self.view.initiate()

    
    def Standard(self):
        self.view.close()
        StandardModelController(self.menuController).initiate()

    def Probabilistic(self):
        self.view.close()
        ProbabilisticModelController(self.menuController).initiate()

    def Discount(self):
        self.view.close()
        discountModelController(self.menuController).initiate()

    def showMenu(self):
        self.view.close()
        self.menuController.show()

from Controllers.ProbabilisticModelController import ProbabilisticModelController
from Controllers.StandardModelController import StandardModelController
from Views.ModelsOptionsView import ModelsOptionsView


class ModelsOptionsController:
    def __init__(self, menuController):
        self.view = ModelsOptionsView(self)
        self.menuController = menuController
    
    def close(self):
        self.view.close()

    def initiate(self):
        self.view.initiate()

    def controlOptions(self, opt):
        if opt == "1":
            self.view.showMessage("1", "1")
        elif opt == "2":
            self.view.showMessage("2", "2")
    
    def Standard(self):
        self.view.close()
        StandardModelController(self.menuController).initiate()

    def Probabilistic(self):
        self.view.close()
        ProbabilisticModelController(self.menuController).initiate()

    def showMenu(self):
        self.view.close()
        self.menuController.show()
from Views.MenuView import MenuView
from Controllers.AbcController import AbcController

class MenuController:
    def __init__(self):
        self.view = MenuView(self)

    def options(self):
        return {
            "1": "Determinar Tipo ABC",
            "2": "Texto2",
            "3": "Texto3",
            "4": "Texto4"
        }
    
    def show(self):
        self.view.show()

    def initiate(self):
        self.view.initiate()

    def controlOptions(self, opt):
        if opt == "1":
            self.view.hide()
            AbcController().show()
        elif opt == "2":
            self.view.showMessage("Opcion","Opcion 2")
        elif opt == "3":
            self.view.showMessage("Opcion","Opcion 3")
        elif opt == "4":
            self.view.showMessage("Opcion","Opcion 4")
import random
from Controllers.AbcController import AbcController
from Views.UserAbcView import UserAbcView


class UserAbcController:
    def __init__(self, menuController):
        self.menuController = menuController
        self.view = UserAbcView(self)

    def show(self):
        self.view.initiate()

    def showMenu(self):
        self.view.close()
        self.menuController.show()

    def solveABC(self):
        try:
            numProd = int(self.view.entryNumeroProductos.get())
            var1 = int(self.view.entryVar1.get())
            var2 = int(self.view.entryVar2.get())
            var3 = int(self.view.entryVar3.get())
            var4 = int(self.view.entryVar4.get())
            data = [[f"{i}", random.randrange(var1,var2), random.randrange(var3,var4)] for i in range(numProd)]
            self.view.close()
            AbcController(self.menuController, data).show()
        except:
            self.view.showMessage("ERROR!", "Formato de Datos Incorrecto\nAsegurese de llenar todos los Campos \ny usar SOLO numero enteros")
        
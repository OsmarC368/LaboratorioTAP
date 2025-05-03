from Models.Models import Models
from Views.TipoDemandaView import TipoDemandaView

class TipoDemandaController:
    def __init__(self, menuController):
        self.view = TipoDemandaView(self)
        self.menuController = menuController
        
    
    def close(self):
        self.view.close()

    def initiate(self):
        self.view.initiate()

    def solve(self):
        try:
            data = list(map(lambda x: int(x), self.view.entryData.get().split(",")))
            self.view.textResult.delete('1.0', "end")
            self.view.textResult.insert('end', f"La Demanda es de Tipo: {Models().tipoDemanda(data)}")
        except:
            self.view.showMessage("ERROR", "Error en la Entrada de Datos")

    

    def showMenu(self):
        self.view.close()
        self.menuController.show()
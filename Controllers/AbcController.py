from Views.AbcView import AbcView

class AbcController:
    def __init__(self):
        self.view = AbcView(self)

    def show(self):
        self.view.show()
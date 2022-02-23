class Posicao():
    def __init__(self):
        self.ocupante = None
    
    def getOcupante(self):
        return self.ocupante
    
    def setOcupante(self, ocupante):
        self.ocupante = ocupante
    
    def ocupada(self):
        return self.ocupante != None
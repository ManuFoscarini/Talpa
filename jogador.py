class Jogador():
    def __init__(self, nome, cor, turno):
        self.nome = nome
        self.cor = cor
        self.turno = turno
        self.vencedor = False

    def setTurno(self, turno):
        self.turno = turno

    def getTurno(self):
        return self.turno

    def setVencedor(self, vencedor):
        self.vencedor = vencedor

    def getVencedor(self):
        return self.vencedor

    def getNome(self):
        return self.nome
        
    def inverteTurno(self):
        self.turno = not(self.turno)
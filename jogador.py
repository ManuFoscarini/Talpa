class Jogador():
    def __init__(self, nome, cor, turno):
        self.nome = nome
        self.cor = cor
        self.seuTurno = turno
        self.vencedor = False
        self.jogando = False


    def setTurno(self, turno):
        self.seuTurno = turno

    def getTurno(self):
        return self.seuTurno

    def setVencedor(self, vencedor):
        self.vencedor = vencedor

    def getVencedor(self):
        return self.vencedor

    def getNome(self):
        return self.nome
        
    def getCor(self):
        return self.cor
        
    def inverteTurno(self):
        self.seuTurno = not(self.seuTurno)

    def setJogando(self, valor):
        self.jogando = valor
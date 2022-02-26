from jogador import Jogador
from posicao import Posicao


class Tabuleiro():
    def __init__(self):
        self.player1 = Jogador("Azul", 0, True)
        self.player2 = Jogador("Vermelho", 1, False)
        self.posicoes = [[], [], [], [], [], [], [], []]
        for i in range(8):
            for j in range(8):
                self.posicoes[i][j] = Posicao()
        self.partidaEmAndamento = True
        self.jogadaEmAndamento = False
        self.pecaRetirada = None

    def ColocarJogoEstadoInicial(self):
        self.colocaPosicoesEstadoInicial()
        self.setPartidaEmAndamento(True)
        self.setJogadaEmAndamento(False)
        self.setMensagem(0)
        self.player1.setTurno(True)
        self.player2.setTurno(False)
        
    def colocaPosicoesEstadoInicial(self):
        for i in range(8):
            for j in range(8):
                if i+j % 2 == 0:
                    self.posicoes[i][j].setOcupante(self.player1)
                else:
                    self.posicoes[i][j].setOcupante(self.player2)

    def setPartidaEmAndamento(self, valor):
        self.partidaEmAndamento = valor

    def setJogadaEmAndamento(self, valor):
        self.jogadaEmAndamento = valor
    
    def setMensagem(self, codigo):
        if codigo == 0:
            self.mensagem = "O jogo esta em andamento"
        #mais opcoes serao adicionadas aqui
    
    def mesmaCor(self, linha, coluna):
        return self.posicoes[linha][coluna].getOcupante().getCor() == self.jogadorDaVez().getCor()
    
    def adjacente(self, linha, coluna):
        return abs(self.pecaRetirada[0] - linha) + abs(self.pecaRetirada[1] - coluna) == 1
    
    def jogadorDaVez(self):
        if self.player1.getTurno():
            return self.player1
        else:
            return self.player2

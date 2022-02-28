from jogador import Jogador
from posicao import Posicao


class Tabuleiro():
    def __init__(self):
        self.player1 = Jogador("Azul", 0, True)
        self.player2 = Jogador("Vermelho", 1, False)
        self.posicoes = [[], [], [], [], [], [], [], []]
        for i in range(8):
            for j in range(8):
                self.posicoes[i].append(Posicao())
        self.partidaEmAndamento = False
        self.jogadaEmAndamento = False
        self.pecaRetirada = None
    
    def SelecionaPosicao(self, linha, coluna):
        if self.partidaEmAndamento:
            self.procederLance(linha, coluna)
        else:
           self.ColocarJogoEstadoInicial()
    
    def procederLance(self, linha, coluna):
        if not(self.jogadaEmAndamento):
            if self.mesmaCor(linha, coluna):
                self.setMensagem(0)
                if self.impossivelComer():
                    self.retiraPeca(linha, coluna)
                    if self.VerificarVencedor():
                        self.setMensagem(2)
                        self.partidaEmAndamento = False
                    else:
                        self.player1.inverteTurno()
                        self.player2.inverteTurno()
                else:
                    self.retiraPeca(linha, coluna)
                    self.pecaRetirada = [linha, coluna]
                    self.jogadaEmAndamento = True

            else:
                self.setMensagem(1)
        else:
            if self.adjacente(linha, coluna):
                if self.mesmaCor(linha, coluna):
                    self.jogadaEmAndamento = False
                    self.posicoes[self.pecaRetirada[0]][self.pecaRetirada[1]].setOcupante(self.jogadorDaVez())
                else:
                    self.posicoes[linha][coluna].setOcupante(self.jogadorDaVez())
                    if self.VerificarVencedor():
                        self.setMensagem(2)
                        self.partidaEmAndamento = False
                    else:
                        self.jogadaEmAndamento = False
                        self.player1.inverteTurno()
                        self.player2.inverteTurno()
            else:
                self.jogadaEmAndamento = False
                self.posicoes[self.pecaRetirada[0]][self.pecaRetirada[1]].setOcupante(self.jogadorDaVez())

    def ColocarJogoEstadoInicial(self):
        self.colocaPosicoesEstadoInicial()
        self.setPartidaEmAndamento(True)
        self.setJogadaEmAndamento(False)
        self.setMensagem(0)
        self.player1.setTurno(True)
        self.player2.setTurno(False)
        self.player1.setVencedor(False)
        self.player2.setVencedor(False)
        
    def colocaPosicoesEstadoInicial(self):
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
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
        elif codigo == 1:
            self.mensagem = "Posicao Invalida"
        elif codigo == 2:
            self.mensagem = f"{self.getVencedor().getNome()} venceu a partida."
        #mais opcoes serao adicionadas aqui
    
    def mesmaCor(self, linha, coluna):
        return self.posicoes[linha][coluna].ocupada() and  self.posicoes[linha][coluna].getOcupante().getCor() == self.jogadorDaVez().getCor()
    
    def adjacente(self, linha, coluna):
        return abs(self.pecaRetirada[0] - linha) + abs(self.pecaRetirada[1] - coluna) == 1
    
    def jogadorDaVez(self):
        if self.player1.getTurno():
            return self.player1
        else:
            return self.player2
    
    def retiraPeca(self, linha, coluna):
        self.posicoes[linha][coluna].setOcupante(None)
    
    def VerificarVencedor(self):
        vencedor1 = False
        vencedor2 = False
        listaPosicoes = []
        matrizAuxiliar = []
        for i in range(8):
            matrizAuxiliar.append([0,0,0,0,0,0,0,0])
        for i in range(8):
            if not(self.posicoes[0][i].ocupada()):
                listaPosicoes.append([0, i])
        while(len(listaPosicoes) > 0):
            posicaoAtual = listaPosicoes.pop(0)
            adjacentes = [[posicaoAtual[0]-1, posicaoAtual[1]], [posicaoAtual[0]+1, posicaoAtual[1]], [posicaoAtual[0], posicaoAtual[1]-1],[posicaoAtual[0], posicaoAtual[1]+1]]
            for i in range(4):
                pos0 = adjacentes[i][0]
                pos1 = adjacentes[i][1]
                if  (0 <= pos0 <= 7) and (0 <= pos1 <= 7):
                    if (not(self.posicoes[pos0][pos1].ocupada()) and matrizAuxiliar[pos0][pos1] == 0):
                        listaPosicoes.append([pos0, pos1])
                        matrizAuxiliar[pos0][pos1] = 1
        for i in range(8):
            if matrizAuxiliar[7][i] == 1:
                vencedor1 = True
                break
        for i in range(8):
            for j in range(8):
                matrizAuxiliar[i][j] = 0
        listaPosicoes = []
        for i in range(8):
            if not(self.posicoes[i][0].ocupada()):
                listaPosicoes.append([i, 0])
        while(len(listaPosicoes) > 0):
            posicaoAtual = listaPosicoes.pop(0)
            adjacentes = [[posicaoAtual[0]-1, posicaoAtual[1]], [posicaoAtual[0]+1, posicaoAtual[1]], [posicaoAtual[0], posicaoAtual[1]-1],[posicaoAtual[0], posicaoAtual[1]+1]]
            for i in range(4):
                pos0 = adjacentes[i][0]
                pos1 = adjacentes[i][1]
                if  (0 <= pos0 <= 7) and (0 <= pos1 <= 7):
                    if (not(self.posicoes[pos0][pos1].ocupada()) and matrizAuxiliar[pos0][pos1] == 0):
                        listaPosicoes.append([pos0, pos1])
                        matrizAuxiliar[pos0][pos1] = 1
        for i in range(8):
            if matrizAuxiliar[i][7] == 1:
                vencedor2 = True
                break
        
        if vencedor1 and vencedor2:
            if self.player1 == self.jogadorDaVez():
                self.player2.setVencedor(True)
            else:
                self.player1.setVencedor(True)
        elif vencedor1 and not(vencedor2):
            self.player1.setVencedor(True)
        elif not(vencedor1) and vencedor2:
            self.player2.setVencedor(True)

        return (vencedor1 or vencedor2)


    def impossivelComer(self):
        for i in range(8):
            for j in range(8):
                posicaoAtual = [i, j]
                adjacentes = [[posicaoAtual[0]-1, posicaoAtual[1]], [posicaoAtual[0]+1, posicaoAtual[1]], [posicaoAtual[0], posicaoAtual[1]-1],[posicaoAtual[0], posicaoAtual[1]+1]]
                for i in range(4):
                    pos0 = adjacentes[i][0]
                    pos1 = adjacentes[i][1]
                    if  (0 <= pos0 <= 7) and (0 <= pos1 <= 7):
                        if (self.posicoes[pos0][pos1].ocupada() and self.posicoes[pos0][pos1] != self.jogadorDaVez()):
                            return False
        return True

    def getMensagem(self):
        return self.mensagem
    
    def getCor(self, linha, coluna):
        if not(self.posicoes[linha][coluna].ocupada()):
            return 2
        elif self.posicoes[linha][coluna].getOcupante() == self.player1:
            return 0
        else:
            return 1
    
    def getVencedor(self):
        if self.player1.getVencedor():
            return self.player1
        else:
            return self.player2

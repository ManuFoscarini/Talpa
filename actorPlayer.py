from tkinter import *
#from tkinter import ttk
from tabuleiro import Tabuleiro
 

#master = Tk()
 
#master.geometry("200x200")


class ActorPlayer:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.mainWindow = Tk()
        self.fillMainWindow()
        self.mainWindow.mainloop()

    def fillMainWindow(self):
        self.mainWindow.title("Talpa")
        self.mainWindow.iconbitmap("images/icon.ico")
        self.mainWindow.geometry("500x550")
        self.mainWindow.resizable(False, False)
        self.mainWindow["bg"] = "white"

        self.mainFrame = Frame(self.mainWindow, padx=32, pady=25, bg="white")
        self.messageFrame = Frame(self.mainWindow, padx=4, pady=1, bg="white")

        self.empty = PhotoImage(file="images/empty.png")  # pyimage1
        self.blue = PhotoImage(file="images/blue.png")  # pyimage2
        self.red = PhotoImage(file="images/red.png")  # pyimage3

        self.boardView = []

        for x in range(8):
            viewTier = []
            for y in range(8):
                aLabel = Label(self.mainFrame, bd=2,
                               relief="solid", image=self.red)
                if (x + y) % 2 == 0:
                    aLabel = Label(self.mainFrame, bd=2,
                                   relief="solid", image=self.blue)
                aLabel.grid(row=x, column=y)
                aLabel.bind("<Button-1>", lambda event, line=x+1,
                            column=y+1: self.click(event, line, column))
                viewTier.append(aLabel)

            self.boardView.append(viewTier)

        self.labelMessage = Label(self.messageFrame, bg="white",
                                  text='Clique em qualquer posição para iniciar', font="arial 14")
        self.labelMessage.grid(row=0, column=0, columnspan=3)
        self.mainFrame.grid(row=0, column=0)
        self.messageFrame.grid(row=1, column=0)

    def click(self, event, linha, coluna):
        print([linha-1, coluna-1])
        self.tabuleiro.SelecionaPosicao(linha-1, coluna-1)
        self.updateUserInterface()
        '''
        label = self.boardView[linha-1][coluna-1]
        if label['imag'] == 'pyimage2':
            label['imag'] = self.empty
            self.whiteTurn = False
        else:
            label['imag'] = self.empty
            self.whiteTurn = True
        '''
    def updateUserInterface(self):
        self.labelMessage['text'] = self.tabuleiro.getMensagem()
        for i in range(8):
            for j in range(8):
                label = self.boardView[i][j]
                cor = self.tabuleiro.getCor(i, j)
                if cor == 0:
                    label['imag'] = self.blue
                elif cor == 1:
                    label['imag'] = self.red
                elif cor == 2:
                    label['imag'] = self.empty

#ttk.Button(master,
            # text ="Click to open a new window",
            # command = ActorPlayer).pack()

#mainloop()

ActorPlayer()



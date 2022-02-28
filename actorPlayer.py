from tkinter import *
from tkinter import ttk
import tabuleiro
import boardImage
 

master = Tk()
 
master.geometry("200x200")


class ActorPlayer:
    def __init__(self):
        self.mainWindow = Tk()
        self.fillMainWindow()
        self.myBoard = tabuleiro.Tabuleiro()
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

        for y in range(8):
            viewTier = []
            for x in range(8):
                aLabel = Label(self.mainFrame, bd=2,
                               relief="solid", image=self.blue)
                if (x + y) % 2 == 0:
                    aLabel = Label(self.mainFrame, bd=2,
                                   relief="solid", image=self.red)
                aLabel.grid(row=x, column=y)
                aLabel.bind("<Button-1>", lambda event, line=y+1,
                            column=x+1: self.click(event, line, column))
                viewTier.append(aLabel)

            self.boardView.append(viewTier)

        self.labelMessage = Label(self.messageFrame, bg="white",
                                  text='Clique em qualquer posição para iniciar', font="arial 14")
        self.labelMessage.grid(row=0, column=0, columnspan=3)
        self.mainFrame.grid(row=0, column=0)
        self.messageFrame.grid(row=1, column=0)

    def click(self, event, linha, coluna):
        self.myBoard.procederLance(linha, coluna)
        self.updateUserInterface()

    def updateUserInterface(self, linha, coluna):
        novoEstado = self.myBoard.setMensagem()
        self.labelMessage['text'] = novoEstado.getMessage()
        label = self.boardView[linha-1][coluna-1]
        for y in range(8):
            for x in range(8):
                label = self.boardView[x][y]
                value = novoEstado.getValue(x+1, y+1)
                if label['imag'] == 'pyimage2':
                    label['imag'] = self.empty
                    self.whiteTurn = False
                else:
                    label['imag'] = self.empty
                    self.whiteTurn = True


mainloop()


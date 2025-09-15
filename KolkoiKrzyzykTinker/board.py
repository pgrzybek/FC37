import tkinter as tk

from checkWinner import checkWinner

from moves import computerMove
from winningLines import victoryLines

moves={}

def updateBoard(btn,sideImage) :
    btn.config(image=sideImage)
    # wyłączenie przycisku
    btn.config(state="disabled")


def blockBoard(buttons):
    for b in buttons:
        b.config(state="disabled")

def resetBoard(buttons,result,n,winningLines,xImage) :
    global moves
    moves={}
    result.configure(text="")
    for b in buttons:
        b.config(image="", state="normal")
    picked = computerMove(n, winningLines, moves)
    updateBoard(buttons[picked], xImage)


def makeBoard(n,root,oImage,xImage,columnSize,rowSize):
    global moves
    def player_click(number):
        #print(f"Kliknięto przycisk {number}")
        pickedBtn = buttons[number]
        moves[number]= "o"
        updateBoard(pickedBtn, oImage)
        print(f" wining lines{winningLines}")
        #print(moves.get(number))
        picked=computerMove(n, winningLines, moves)
        moves[picked]= "x"
        print(f" wining lines{winningLines}")
        pickedBtn = buttons[picked]
        updateBoard(pickedBtn, xImage)
        if len(moves)>2:
            if checkWinner(moves, winningLines) == "o":
                result.config(text="wygrana")
                blockBoard(buttons)
            if checkWinner(moves, winningLines) == "x":
                result.config(text="przegrana")
                blockBoard(buttons)


    buttons = []  # lista przechowująca przyciski
    counter = 0
    winningLines = victoryLines(n)
    buttonsFrame = tk.Frame(root)
    buttonsFrame.pack(side="bottom")
    result = tk.Label(root, text="")
    result.pack()
    for r in range(n):
        #row_buttons = []
        for c in range(n):
            #counter = r * n + c
            btn = tk.Button(buttonsFrame, text=str(counter), #width=10, height=5,
                                          command=lambda num=counter: player_click(num))
            btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
            buttons.append(btn)
            #row_buttons.append(btn)
            counter += 1

    # Ustawienie wymiarów w gridzie, aby każdy przycisk miał ~100x100 px
    for i in range(n):
        buttonsFrame.grid_columnconfigure(i, minsize=columnSize)
        buttonsFrame.grid_rowconfigure(i, minsize=rowSize)


    move = computerMove(n, winningLines, moves)
    moves[move] = "x"
    updateBoard(buttons[move],xImage)
    return buttons,result

import tkinter as tk
from board import makeBoard, resetBoard

from winningLines import victoryLines

# def przycisk_klik():
#     print("Przycisk kliknięty!")

root = tk.Tk()
#global n
n=3

sizeStart=110
sizeWidth=n*sizeStart
sizeHeight=n*sizeStart+50
size=str(f"{sizeWidth}x{sizeHeight}")
root.geometry(size)

root.title("Kolko i krzyzyk")
oImage = tk.PhotoImage(file="o.gif")
xImage = tk.PhotoImage(file="x.gif")
frame=tk.Frame(root)
frame.pack(side="bottom")
buttons,result=makeBoard(n,frame,oImage,xImage,sizeStart,sizeStart)
reset=tk.Button(root,text="Reset",command=lambda buttons=buttons, result=result :resetBoard(buttons,result))
reset.pack()
#reset.grid(row=1, sticky="nsew", padx=2, pady=2)

#resetBoard(buttons,moves)
#print(victoryLines(3))
root.mainloop()
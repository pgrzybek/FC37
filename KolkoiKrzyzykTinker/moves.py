import random
import sys
import copy
linePicked=[]
linesNotUsed = []


def get_random_int(min_val, max_val):
    return random.randint(min_val, max_val)


def pickline(linesUsedNot, move):
    global linePicked
    for line2 in linesUsedNot:
        if move in line2:
            linePicked = line2.copy()
            linePicked.remove(move)
            break

    return linePicked

def checkLine(moves, lineToCheck):
    values = [moves.get(key) for key in lineToCheck]
    unique = set(values)
    #if "x" in unique and None in unique:
    if "o" not in unique:
            for i in range(len(values)):
                if values[i] is None:
                    print(i)
                    move = i
                    return move
    else: pass # zmien cholerna linie

    return None



def computerMove(n,winningLines,moves):
    # zrob losowy ruch
    # wybierz linie
    # sprawdz linie czy nie ma ruchu przeciwnika
    # jesli jest wybierz linie odrzuc linie
    # jesli nie dodaj ruch w linii
    boardSize=n*n
#     let move;
    move=0

    global linePicked
    global linesNotUsed
    #linePicked=[]
    if len(moves)==0:
        linesNotUsed=[]
        linesNotUsed=copy.deepcopy(winningLines)
        move = get_random_int(0, boardSize - 1)
        linePicked=pickline(linesNotUsed,move)
        print(f"linesNotUsed:{linesNotUsed}")
        return move
       # print(f"linePicked={linePicked}")
    else:
            #wybierz linie
            if len(linePicked) > 0:
                values = [moves.get(key) for key in linePicked]
                unique = set(values)
                # if "x" in unique and None in unique:
                if "o" not in unique:
                    move=next(iter(linePicked))
                    linePicked.remove(move)
                # if checkLine(moves,linePicked):
                #     move=checkLine(moves,linePicked)
            else:
                    #do poprawy
                    linePicked=[]
                    move = get_random_int(0, boardSize - 1)
                    linePicked = pickline(linesNotUsed,move)
                        #if "x" in unique and None in unique:
                    print(f"linePicked={linePicked}")

                    #jezeli jest o  w uniqu znajdz nowa linie
                    # result = next(iter(unique))
                    # if result == None:
                    #     index=unique
                    #print(result)

                    #bierz nastepna wartosc z linepiked
                    #sprawdz guzik czy jest pusty

                #     result = next(iter(unique))
                #     print(f"result {result}")
                #     if  not result :
                #         move=linePicked
                #     break
            # else:
            #     move=get_random_int(0,boardSize-1)
            #     values = [moves.get(key) for key in line]
            #     unique = set(values)
            #     print(f"if2 {unique}")
            #     if  "x" in unique and None in unique:
            #         result = next(iter(unique))
            #         if result:
            #             move = linePicked.index(result)
            #             linePicked = line
            #         break
        #move = moves[move]
    return move

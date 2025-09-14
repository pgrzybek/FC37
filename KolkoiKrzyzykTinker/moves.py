import random

def get_random_int(min_val, max_val):
    return random.randint(min_val, max_val)
linePicked=[]

def pickline(winningLines,boardSize):
    global linePicked
    move = get_random_int(0, boardSize - 1)
    for line in winningLines:
        if move in line:
            linePicked = line
            break
    return move

def computerMove(n,winningLines,moves):
    boardSize=n*n
#     let move;
    move=0
    global linePicked
    #linePicked=[]
    if len(moves)==0:
        move=pickline(winningLines,boardSize)

        print(f"linePicked={linePicked}")
    else:
        #for line in winningLines:
            if len(linePicked) > 0:
                values = [moves.get(key) for key in linePicked ]
                unique = set(values)
                #print(line)
                # print(f"if1 {unique}")
                # print(f"if1 {linePicked}")
                # print(values)
                # print(moves)
                if "o" not in unique:
                    for i in range(len(values)):
                        if values[i] is None:
                            move=i
                else:
                    #do poprawy
                    move=pickline(winningLines,boardSize)
                    print(f"linePicked={linePicked}")

                    #jezeli jest o uniqu znajdz nowa linie
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

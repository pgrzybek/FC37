def checkWinner(moves,winningLines) :
    for  line in winningLines :

        values=[]
        values = [moves.get(i) for i in line]
        unique = set(values)
    # sprawdzenie warunku

        if len(unique) == 1 and None not in unique:  # Python używa None zamiast undefined
           result = next(iter(unique))  # pobiera jedyną wartość ze zbioru
           return result
        #print(result)  # np. "X" albo "O"
    return None# brak zwycięzcy

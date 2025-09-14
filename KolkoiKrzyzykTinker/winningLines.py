def victoryLines(n):
     # przykładowy rozmiar planszy
    lines = []

    for r in range(n):
        line = [(r * n + i ) for i in range(n)]
        lines.append(line)

    for c in range(n):
        line=[(i * n + c ) for i in range(n) ]
        lines.append(line)
    #diag_main = [i * n + i for i in range(n)]

     # przekątna odwrotna: 2,4,6
    #diag_anti = [i * n + (n - 1 - i) for i in range(n)]

    lines.append([(i * n + (n - 1 - i))for i in range(n)])
    lines.append([(i * n + i) for i in range(n)])
    return lines


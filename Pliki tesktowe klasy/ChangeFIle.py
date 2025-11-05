from ReadFile import ReadFile
from WriteFile import WriteFile



class ChangeFile(ReadFile):
    """
    Tu zmieniamy wartosc szukana i wywolujemy zapis
    """
    def __init__(self, filepath,searched):
        super().__init__(filepath,searched)
        self.searched = searched

    def changePOS(self,posX,posY,value):
        if 0 <= posX < len(self.lines):  # sprawdz czy pozycje sa wieks
                if 0 <= posY < len(self.lines[posX]):
                    self.lines[posX][posY] = value
                    #print(fileContent)
                else:
                    print("Nie ma tyle kolumn")
                    choiceKolumn = input("Dodac kolumne ? (t/n)")
                    if choiceKolumn == "t":
                        self.lines[posX].append(value)
                        print("Wartosc zostala dodana na kolejnej pozycji")
        # for i in range(posX):
        #     for j in range(posY):
        #         self.lines[i][j] = toReplace

    def printOut(self):
        print("File contents is ")
        for row in self.lines:
            print("\n")
            for item in row:
                print(item, end=" ")

# infile="files/out.txt"
# posx=1
# posy=2
# value="cos"
# outfile2="in.txt"
# change=ChangeFile(infile,"")
# print(change.lines)
# change.changePOS(posx,posy,value)
# writer=WriteFile(outfile2,change.lines)
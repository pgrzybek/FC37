import csv
import os
import sys

message="Za malo parametrow 1 do plik do czytania drugi plik zapisu 3 to pozycja wiersza 4 pozycja kolumny  5 to wartosc"
if len(sys.argv) > 1:
    infile=sys.argv[1]
else:
    sys.exit(message)

if len(sys.argv) > 2:
    outfile=sys.argv[2]
else:
    sys.exit(message)
if len(sys.argv) > 3:
    posX=int(sys.argv[3])
else:
    sys.exit(message)

if len(sys.argv) > 4:
    posY=int(sys.argv[4])
else:
    sys.exit(message)

if len(sys.argv) > 5:
    value=sys.argv[5]
else:
    print(message)
    sys.exit(message)
if len(sys.argv) <1:
    sys.exit(message)
#infile=sys.argv[1]

#infile= input("Enter the file name : ")
#infile= infile +".csv"
#outfile=".csv".join(file)
#print(infile)
#print(outfile)
#infile="my_csv_file.csv"
#outfile="my_csv_file.csv"
#filContent=[]

#outfile = "dane"        # albo "dane.csv"
def checkExtension(file):
    name, ext = os.path.splitext(file)

    if ext.lower() != ".csv":
        file = name + ".csv"
    return file
infile=checkExtension(infile)
outfile=checkExtension(outfile)
#posY=0
# posX=int(input("Enter the X coordinate of the position: "))
# posY=int(input("Enter the Y coordinate of the position: "))
# value=(input("Enter value: "))
def fileDontExist(StartValue,file):
    choice = input("Plik nie zostal znaleziony chcesz utworzyc nowy? (t/n)")
    if choice == "t":
        with open(file, "w", newline="") as f2:
            fileWriter = csv.writer(f2, delimiter=";")  # excel odczekuje ";" jako separator
            fileWriter.writerows(StartValue)
    else:
        sys.exit()


def printOut(file_content):
    print("File contents is ")
    for row in file_content:
        print("\n")
        for item in row:
            print(item, end=" ")



if os.path.exists(infile):
    with open(infile, newline="") as f:
        fileReader = csv.reader(f, delimiter=";")
        fileContent = list(fileReader)
        if 0 <= posX < len(fileContent):    #sprawdz czy pozycje sa wieks
            if 0 <= posY < len(fileContent[posX]):
                fileContent[posX][posY] = value
                #print(fileContent)
            else:
                print("Nie ma tyle kolumn")
                choiceKolumn = input("Dodac kolumne ? (t/n)")
                if choiceKolumn == "t":
                    fileContent[posX].append(value)
                    print("Wartosc zostala dodana na kolejnej pozycji")

        else:
            print("Nie ma tyle wierszy")
            choiceKolumn = input("Dodac wiersz ? (t/n)")
            if choiceKolumn == "t":
                #print(fileContent)
                row=[value]
                fileContent.append(row)
                print("Wartosc zostala dodana na kolejnej pozycji")
                #print(fileContent)
        #re[1] = ["Jan", "Kowalski", "45"]
    if os.path.exists(outfile):
        with open(outfile, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerows(fileContent)
            # for i in  range(len(fileContent)):
            #     writer.writerows(fileContent[i])
        printOut(fileContent)
            #print(fileContent)
    else:
        fileDontExist(fileContent,outfile)
else:
    start=[]
    row = [value]
    start.append(row)
    fileDontExist(start,infile)

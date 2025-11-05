import csv
import json
import os
import sys
import tempfile


from BaseFile import BaseFile
from ReadFile import ReadFile
import shutil


class WriteFile(BaseFile):
    """
    klasa zapisujaca
    przerabiamy wartosci z self.lines na wartosci innego pliku
    z tekstowego przerabiamy wartosci na slownik a ze slownika na liste tekstowa
    na koncu zapisujemy to do nowego pliku i robimy shutil.move
    shutil.move(dane.tmp,plik.rozszerzenie
    filepath : sciezka do pliku
    delimiter: znak rozdielajacy
    """

    def __init__(self, filepath,data):
        super().__init__(filepath)
        #self.tempFile = tempfile.TemporaryFile().name
        self.tempFile="dane.temp"
        self.lines = data
        self.write()
    @staticmethod
    def fileDontExist(StartValue, file):
        choice = input("Plik nie zostal znaleziony chcesz utworzyc nowy? (t/n)")
        if choice == "t":
            with open(file, "w", newline="") as f2:
                fileWriter = csv.writer(f2, delimiter=";")  # excel odczekuje ";" jako separator
                fileWriter.writerows(StartValue)
        else:
            sys.exit()
    @staticmethod
    def decorateWrite(met):
        """
        Metoda opisujaca do zapisywania plikow dziala na metodach klasy
        Parametr self w wrapper odsosi sie do atrybutu self klasy
        :param met: metoda ktora przetwarza plik
        :return:  swoja metode
        """
        def wrapper2(self, *args, **kwargs):
            with open(self.tempFile, "w") as f:
                met(self, *args, **kwargs, f=f)
        return wrapper2


    def write(self):
        if os.path.exists(self.filepath):
            extension = self.checkExtension()
            if extension == ".csv":
                self.writeCsv()
            if extension == ".json":
                self.writeJson()
            if extension == ".txt":
                self.writetxt()
            if extension == ".pickle":
                self.writePickle()
        else:
            choice = input("Plik nie istnieje stworzyc t/n")
            if choice == "t":
                with open(self.filepath, "w") as f:
                    f.write(" ")
            else:
                sys.exit()

    def writetxt(self):
        """
        Zapisz to co jest w lines do pliku tekstowego self.tempfile
        Jesli puste  zapisz pusty znak tworzac nowy plik
        :return:

        """
        if not os.path.exists(self.filepath):
            with open(self.tempFile, "w") as f:
                f.write(" ")
        with open(self.tempFile, "w") as f:
            if not self.lines:
                f.write(" ")
            else:
                for line in self.lines:
                    for i in range(len(line)):
                        f.write(line[i])
                        if i<len(line)-1:
                            f.write(self.delimiter)
                    f.write("\n")
        shutil.move(self.tempFile, self.filepath)

    def writeCsv(self):
        with open(self.tempFile, "w" ,newline='') as f:
            writer= csv.writer(f)
            if not self.lines:
                writer.writerow([])
            else:
                for line in self.lines:
                    writer.writerow(line)
        shutil.move(self.tempFile, self.filepath)

    def writeJson(self):
        with open(self.tempFile, "w",newline='') as f:
            json.dump(self.lines, f)
        shutil.move(self.tempFile, self.filepath)

    def writePickle(self):
        with open(self.tempFile, "w",newline='') as f:
            json.dump(self.lines, f)
        shutil.move(self.tempFile, self.filepath)


#
# r=ReadFile("files/out.txt","")
#
# w=WriteFile("files/plik.json", r.lines)




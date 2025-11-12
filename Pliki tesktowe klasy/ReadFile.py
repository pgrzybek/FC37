import csv
import functools
import json
import os
import pickle

import logging
import sys

from BaseFile import BaseFile

logging.basicConfig(
    level=logging.INFO,  # minimalny poziom logów
    format="%(asctime)s [%(levelname)s] %(message)s",  # format wiadomości
    handlers=[
        # logging.FileHandler("files/app.log"),      # zapis do pliku
        logging.StreamHandler()  # oraz na konsolę
    ]
)

logger = logging.getLogger("MyLogger")


class ReadFile(BaseFile):

    def __init__(self, filepath, searched):
        # self.fp = open(filepath)
        super().__init__(filepath)
        self.searched = searched
        self.load()

    @staticmethod
    def decorateLoad(met):
        """
        Metoda opisujaca do ladowania plikow dziala na metodach klasy
        Parametr self w wrapper odsosi sie do atrybutu self klasy
        :param met: metoda ktora przetwarza plik
        :return:  swoja metode
        """

        def wrapper2(self, *args, **kwargs):
            try:
                with open(self.filepath, "r") as f:
                    met(self, *args, **kwargs, f=f)
            except FileNotFoundError:
                print("File not found write in it first")
                logger.error("File not found write in it first")

        return wrapper2

    #
    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)

    def __getitem__(self, item):
        dictLine = dict(self.foundLine)
        return dictLine[item]

    def __call__(self, *args, **kwargs):
        return self.lines

    # probuje sobie dekoratory

    def __iter__(self):
        # if self.done:
        if self.lines:
            return iter(self.lines)
        else:
            return []
        # return self

    def __len__(self):
        return len(self.lines)

    def load(self):
        if os.path.exists(self.filepath):
            extension = self.checkExtension()
            if extension == ".csv":
                self.loadcsv()
            if extension == ".json":
                self.loadjson()
            if extension == ".txt":
                self.loadtxt()
            if extension == ".pickle":
                self.loadPickle()
        else:
            choice = input("Plik nie istnieje stworzyc t/n")
            if choice == "t":
                with open(self.filepath, "w") as f:
                    f.write(" ")
            else:
                sys.exit()

    @decorateLoad
    def loadtxt(self, f):
        """
        Ładuje plik do momentu znalezienia wartosci
        :param f:wewnetrzny parametr nie do uzytku
        :return:
        # """
        result = self.searched

        for line in f:
            splited = line.split(self.delimiter)
            splited[-1] = splited[-1].strip()  # usuwa ostatni element czyli znak konca lini
            self.lines.append(splited)
            # del self.lines[0][-1]
            if result in line and result != "":
                self.found = True
                self.foundLine.append(splited)
                # del self.foundLine[0][-1]#usuwa ostatni element czyli znak konca lini
                break

    @decorateLoad
    def loadcsv(self, f):

        reader = csv.reader(f, delimiter=self.delimiter)
        # self.loadloop(reader)
        for line in reader:
            self.lines.append(line)
        self.checkLoop()

    def checkLoop(self):
        result = self.searched
        for line in self.lines:
            if result in line and result != "":
                self.found = True
                self.foundLine = line

    @decorateLoad
    def loadjson(self, f):
        try:
            self.lines = json.load(f)
            self.checkLoop()
        except json.decoder.JSONDecodeError:
            print("To nie plik json")
            logger.log(logging.ERROR, "To nie plik json")

    @decorateLoad
    def loadPickle(self, f):
        try:
            self.lines = pickle.load(f)
            self.checkLoop()
        except pickle.UnpicklingError:
            print("To nie plik pickle")
            logger.log(logging.ERROR, "To nie plik pickle")

    def my_generator(self):
        for i in range(len(self.lines)):
            yield i

# r = ReadFile("files/out.txt","Jan")
#
# print(r.foundLine)
# print(r.lines)
# r.loadcsv()
# print(r.lines)
# r.loadjson()
# print(r.lines)
# i=0
# for i in range(len(r)):
#     print(f"i to {i} wartosc to {r.lines[i]}")

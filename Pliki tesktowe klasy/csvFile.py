import os
import csv
from FileCache import FileCache
from ReadFile import ReadFile
# gdy znajdziesz wpisz do  pamieci podrzeczniej linijke i miejsce a  nastepnie zapisz

class CsvFile(ReadFile):
    def __init__(self, filepath):
        super().__init__(filepath)
        #self.filename = filename
        self.file=""

    def load(self):
        pass

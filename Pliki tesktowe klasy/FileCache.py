import os

from FileReader import FileReader


class FileCache(FileReader):

    def readchar(self, position):
        if position not in self.lines:
            self.fp.seek(position)
        self.lines[position] = self.fp.read(1)
        self.fp.readline()

    def checkExtension(self,extension):
        name, ext = os.path.splitext(self.fp.name)
        if ext.lower() != extension:
            self.fp = name + extension
        return self.fp
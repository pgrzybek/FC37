import os


class FileReader:
    def __init__(self, filepath):
        self.fp = open(filepath)
        self.lines = []
        self.done = False

    def checkExtension(self,extension):
        name, ext = os.path.splitext(self.fp.name)
        if ext.lower() != extension:
            self.fp = name + extension
        return self.fp

    def __iter__(self):
        if self.done:
            return iter(self.lines)
        return self

    def __next__(self):
        line = self.fp.readline()
        if not line:
            self.done = True
            self.fp.close()
            raise StopIteration
        self.lines.append(line[:-1])
        return line[:-1]


r=FileReader("files/plik.csv")
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
#shutil
for line in r:
    print(line)
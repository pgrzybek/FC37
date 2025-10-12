import functools
import os
import shutil


class ReadFile:
    filepath = None

    def __init__(self, filepath):
        # self.fp = open(filepath)
        self.filepath = filepath
        self.lines = []
        self.load()
        self.searched = ""
        self.func = ""

    @staticmethod
    def decorateLoad(func):
        def wrapper2(self, *args, **kwargs):

            f = 2
            self.lines.append(f)
            func(self, *args, **kwargs, f=f)
        return wrapper2
    #
    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)

    # self.done = False
    def __call__(self, *args, **kwargs):
        pass
        # print("cos działą")
        # f = 2
        # self.lines.append(f)
        # return self.func(self, *args, **kwargs, f=f)
        #

    def checkExtension(self):
        name, ext = os.path.splitext(self.filepath.name)
        # if ext.lower() != extension:
        #     self.fp = name + extension
        return ext

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

    @decorateLoad
    def load(self, f):
        print(f)

        # if self.checkExtension()==".csv":
        #     self.loadcsv()
        # if self.checkExtension()==".json":
        #     self.loadjson()

    def loadcsv(self):
        pass

    def loadjson(self):
        pass

    def my_generator(self):
        for i in range(len(self.lines)):
            yield i


r = ReadFile("plik.csv")
ReadFile.filepath="plik.csv"
i=0
for i in range(len(r)):
    print(r.lines[i])

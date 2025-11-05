import os


class BaseFile:
    def __init__(self, filepath):
    # self.fp = open(filepath)
        self.delimiter = ','
        self.filepath = filepath
        self.lines = []
        self.searched = ""
        self.found = False
        self.foundLine=[]
        self.posX=0
        self.posY=0

    def checkExtension(self):
        name, ext = os.path.splitext(self.filepath)
        # if ext.lower() != extension:
        #      self.filepath = name + extension
        return ext
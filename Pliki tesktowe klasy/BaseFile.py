class BaseFile:
    def __init__(self, filepath):
    # self.fp = open(filepath)
        self.delimiter = ','
        self.filepath = filepath
        self.lines = []
        self.searched = ""
        self.found = False
        self.foundLine=[]
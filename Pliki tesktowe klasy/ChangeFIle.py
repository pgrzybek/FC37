from ReadFile import ReadFile


class ChangeFile(ReadFile):
    """
    Tu zmieniamy wartosc szukana i wywolujemy zapis
    """
    def __init__(self, filepath,searched,toReplace):
        super().__init__(filepath)
        self.searched = searched

    def change(self,searched,toReplace):
        pass
    #TODO zrobic wartosc szukana
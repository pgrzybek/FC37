from Athlete import Athlete
from Student import Student

# klasa pochodna z dziedziczeniem wielokrotnym
class StudentAthlete(Student,Athlete):
    def __init__(self,name):
        super().__init__(name) #wywolywanie w kolejnosci MRO

    def introduce(self):
        print(f"Czesc to ja atleta i student {self.name} ")
from Athlete import Athlete
from Student import Student
from StudentAthlete import StudentAthlete

def introduce_person(person):
    person.introduce()


s1=  Student("Jan")
a1 = Athlete("Marek")
sa1 = StudentAthlete("Anna")
s1.introduce()
a1.introduce()
sa1.introduce()

introduce_person(sa1)
introduce_person(s1)
introduce_person(a1)
from  Athlete2 import Athlete2
from Student2 import Student2


class StudentAthlete2(Athlete2,Student2):
    def __init__(self,name,student_id,sport,team,):
        Student2.__init__(self,name,student_id)
        Athlete2.__init__(self,sport,team)

    def showProfile(self):
        print(f"  Name {self.name}, ID {self.student_id}"  )
        print(f"  Team {self.team}, Sport {self.sport}" )


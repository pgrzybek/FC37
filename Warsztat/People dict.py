import json
import os
import logging
logging.basicConfig(level=logging.ERROR)

MyLoger=logging.getLogger(__name__)

class People:
    def __init__(self,filename="people.json"):
        self.filename = filename
        self.data = {}
        self.loadFromFile()
    def __setitem__(self,username,info):
        self.addperson(username,info)
    def __getitem__(self,username):
        print(f"odczytuje dane ze slownika {username}")
        return self.data[username]

    def __iter__(self):
        # Pozwala iterować po nazwach użytkowników
        return iter(self.data)
    def __str__(self):
        return self.filename

    def addperson(self, username,info:dict):
        self.data[username] = info
        self.save_To_File()

    def loadFromFile(self):
        if os.path.exists(self.filename):
            with open(self.filename) as f:
                try:
                    self.data = json.load(f)
                except json.decoder.JSONDecodeError:
                    MyLoger.error("Json broken")

    def save_To_File(self):
        with open(self.filename, 'w',encoding="utf-8") as f:
            json.dump(self.data,f,ensure_ascii=False,indent=4)

if __name__ == "__main__":
    people = People()
    people.addperson("john",{"name":"John","age":30})
    people["john"]={"name":"John","age":30,"city":"Warsaw"}
    print(people["john"])

            #sprawdz czy istnieje
        #załaduj do słownika
        #obsluz wyjatek
    for username in people.data:
        print(username,people.data[username])
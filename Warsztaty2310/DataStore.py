from datetime import datetime

class DataStore:
    def __init__(self,name,description):
        self.name=name
        self.created_at=datetime.now()
        self.description=description
        self.data={}
    def __setitem__(self, key, value):
        self.data[key]=value
    def __getitem__(self, key):
        return self.data[key]
    def __iter__(self):
        return iter(self.data)
    def items(self):
        return self.data.items()
    def __str__(self):
        return f"Datastore  {self.name} , {self.description}"

# d1=DataStore("d1","bbbb")
# print(d1)
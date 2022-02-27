class AllStaff:
    def __init__(self,name,age,id,birthdate,job):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate
        self.job = job

    def show(self):
        print(f"Name:{self.name}"
              f"ID : {self.id}"
              f"age: {self.age}"
              f"birthdate: {self.birthdate}"
              f"job: {self.job}")

class Management(AllStaff):
    def __init__(self,name,age,id,birthdate,job,car):
        super().__init__()

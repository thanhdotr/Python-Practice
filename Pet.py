class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Cat:
    def speak(self):
        print("Meow")


class Dog:
    def speak(self):
        print("Bark")

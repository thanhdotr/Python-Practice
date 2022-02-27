class Dog:
    def __init__(self,name,age,colour):
        self.name = name
        self.age = age
        self.colour = colour
    def print_details(self):
        return(f"{self.name} is a {self.colour} dog aged {self.age}")
    def change_age(self,new_age):
        self.age = new_age
# Main Routine
dog1 = Dog("spot",5,"red")
dog2 = Dog("Jack",6,"blue")

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))

dog1.change_age(17)
dog2.change_age(21)

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))

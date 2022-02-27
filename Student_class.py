class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
class Course:
    def __init__(self,name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self,student):
        if len(self.students):
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
            return total/len(self.students)

#instantiate 3 student object
s1 = Student("Tim",19,95)
s2 = Student("Bill",19,75)
s3 = Student("Jill",19,65)

course1 = Course("Computer Science",1)

course1.add_students(s1)
course1.add_students(s2)



print(f"The average grade is {course1.name} is {course1.get_average_grade()}")

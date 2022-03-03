class Student:
    def __init__(self, name, age, phone_number, form_class, subjects, is_male):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = subjects.replace(" ", "").split(',')
        self.is_male = is_male
        self.enrolled = True
        students_list.append(self)

    def display_info(self):
        print('Full name:', self.name)
        print('Age:', self.age)
        print('Phone number:', self.phone_number)
        print('Form class:',self.form_class)
        print('Classes:', self.subjects)
        if self.is_male:
            gender = 'Male'
        else:
            gender = 'Female'
        print('Gender:', gender)
        print('Enroll:', self.enrolled)
        print('\n***********************************\n')

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        teachers_list.append(self)

    def display_info(self):
        print('Teacher name:', self.name)
        print('Teaching class:', self.subject)
        print('\n***********************************\n')

# generate students from csv file.
def generate_students():
    # available form classes are: "BAKER", "MORGAN", "MCNICOL", "GRAHAM", "BELL", "NIMMO", "BARKER"
    # available classes are: "ART", "ENG", "MAT", "GRA", "DTC", "PHY", "BIO"
    import csv

    with open('random_students.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')

        for line in filereader:

            if line[5] == "True":
                is_male = True
            else:
                is_male = False

            Student(line[0], int(line[1]), line[2], line[3], line[4], is_male)

def print_teacher_details():
    for teacher in teachers_list:
        teacher.display_info()

def print_student_details(student):
    student.display_info()

def select_student_age():
    count = 0
    get_age = int(input('Enter an age to print all students at that age or older: '))

    for student in students_list:
        if student.age >= get_age:
            student.display_info()
            count += 1
    print()
    if count == 0:
        print(f'There are no students at the age of {get_age} or older')
    else:
        print(f'Total: {count} students')
    print()

def count_students():
    count = 0
    teacher_name = ''

    class_code = input('What class are you looking for?\n'
                       '>>> ').upper()

    for student in students_list:
        for subject in student.subjects:
            if class_code == subject:
                count += 1

    for teacher in teachers_list:
        if class_code == teacher.subject:
            teacher_name = teacher.name
    print()

    if count == 0:
        print(f"There are not any classes called {class_code}")
    else:
        print(f'There are {count} students in {class_code} class')
        print('Class teacher:', teacher_name)

    print()

def find_student():
    student_name = input('Name: ').title()
    print()

    for student in students_list:
        if student_name in student.name:
            return print_student_details(student)
    else:
        print(f'There are no student named "{student_name}" in the system.')
    print()

def add_student():
    name = input("Enter student's name: ").title()
    age = int(input("Enter student's age: "))
    phone_number = input("Enter student's phone number: ")
    form_class = input("Enter student's form class: ").upper()
    subjects = input("Enter all student's subjects\n"
                     " * Separate each subject with a comma and a space *\n"
                     ">>> ")
    gender = input("Enter student's gender: ").lower()

    if gender == 'm' or gender == 'male':
        is_male = True
    else:
        is_male = False

    Student(name, age, phone_number, form_class, subjects, is_male)

def delete_student():
    name = input("Enter the student's name who will be terminated: ").title()

    for student in students_list:

        if name in student.name:
            confirm = input(f"Do you want to delete '{student.name}' out of the system?\n"
                             "*** This action cannot be undone ***\n"
                             "Confirm (Y/N): ").upper()

            if confirm == 'Y':
                students_list.remove(student)
            else:
                break

    else:
        print(f'There are no student named "{name}" in the system.')
    print()

def menu():
    action = True

    while action:
        input("Press 'Enter' to open the Menu:")
        print()

        print('**************** MAIN MENU ****************')
        print()
        print('1. Count students taking a particular subject\n'
              '2. Print a full list of all students\n'
              '3. Print a list of students above a particular age\n'
              '4. Get details of a particular student\n'
              '5. Add a new student\n'
              '6. Remove a student\n'
              '7. Print a full list of all teachers')
        print()

        option = input('What would you like to do?\n'
                       ' - Enter a number or "X" to exit -\n'
                       '>>> ').upper()
        print()

        if option == '1':
            count_students()
        elif option == '2':
            for students in students_list:
                print_student_details(students)
        elif option == '3':
            select_student_age()
        elif option == '4':
            find_student()
        elif option == '5':
            add_student()
        elif option == '6':
            delete_student()
        elif option == '7':
            print_teacher_details()
        elif option == 'X':
            action = False
        else:
            print('* Enter a number or "X" to exit *')

#Main routine
teachers_list = []
students_list = []

Teacher('Baker', 'GRA')
Teacher('Barker', 'MAT')
Teacher('Graham', 'BIO')
Teacher('Morgan', 'DTC')
Teacher('Bell', 'PHY')
Teacher('Nimmo', 'ART')
Teacher('McNicol', 'ENG')

generate_students()

menu()


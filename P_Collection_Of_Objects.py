

class Student ():
    def __init__(self, name, course, year, section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def introduceYourself(self):
        print(f"     Name: {self.name}\n"
            f"     Year: {self.year}\n"
            f"     Course: {self.course}\n"
            f"     Section: {self.section}")

studentList = []


while True:
    print ("Student Form")
    name = input(str("Name: "))
    course = input(str("Course: "))
    year = input(str("Year: "))
    section = input(str("Section: "))
    print ()

    #Creating the student record through class
    student = Student (name.title(), course.upper(), year.title(), section.title())

    #Appending the record
    studentList.append(student)

    input_continue = str(input("Continue? Type Y [YES] or [N] No: "))

    if input_continue.upper() == "Y":
        continue

    elif input_continue.upper() == "N":
        print ("Thank you!")
        break

    else:
        print ("Invalid input")
        print ("Exiting the system")
        break

studentnumber = 1
for everystudent in studentList:
    print (f"Student # {studentnumber}\n")
    everystudent.introduceYourself()
    studentnumber = studentnumber + 1
    print()
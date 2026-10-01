#PARENT CLASS
class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def introduce (self):
        print (f"Hi I am {self.firstName} {self.lastName}")

#CHILD CLASS
class Student (Person):
    def __init__(self, firstName, lastName, year, course, section):
        super().__init__(firstName, lastName)
        self.year = year
        self.course = course
        self.section = section

    # OVER-RIDING A PARENT FUNCTION FROM CHILD FUNCTION
    # It Will Override the Function and Can Call the Additional Parameters
    # def introduce (self):
    #     print (f"Hi! My name is {self.firstName} {self.lastName} and I am in {self.year} taking {self.course}")

    # RETAIN THE PARENT FUNCTION PERO GUSTO DAGDAGAN, use SUPER()
    def introduce(self):
        print("/////////")
        super().introduce()
        print (f"From {self.course} for the year {self.year}")

    

#PARENT
personOne = Person ("Gelo", "Reyes")
personOne.introduce()

#STUDENT
studentOne = Student ("Gelo","Reyes", "4th year", "BSIE", "Sample-Section")
studentOne.introduce()

print (studentOne.lastName)
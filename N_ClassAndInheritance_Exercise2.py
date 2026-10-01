#PARENT CLASS
class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def introduce (self):
        print (f"Hi I am {self.firstName} {self.lastName}")


class Employee (Person):
    def __init__(self, firstName, lastName, salary):
        super().__init__(firstName, lastName)
        self.salary = salary

    def introduce(self):
        super().introduce()
        print (f"My Salary is {self.salary}")
        print()

employeeOne = Employee("Gelo", "Reyes", "P 90,000")

employeeTwo = Employee("Karen", "Basco", "P100,000")

employeeThree = Employee ("Pepito", "Manaloto", "P1,000,000")

employeeOne.introduce()
employeeTwo.introduce()
employeeThree.introduce()
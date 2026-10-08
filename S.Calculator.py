

numbers = []
ops = ["[1] Addition", "[2] Subtraction", "[3] Multiplication", "[4] Division"]


# Calculator Class
class Calculator ():
    def __init__(self, operations, numbers, answer):
        self.numbers = numbers
        self.answer = answer
        self.operations = operations

    def more (self):
        more = int(input("Add more? [Y] Yes or [N] No: "))

        if more.upper() == "Y":
            return True

        elif more.upper() == "N":
            return False

        else:
            print ("Invalid Input")



    def add (self):
        while True:
            numberToAdd = int(input("Enter number: "))
            numbers.append (numberToAdd)

            for everynumber in numbers:
                print (f"{everynumber} + ")


            if not self.more ():
                break

    def subtract (self):
        while True:
            numberToAdd = int(input("Enter number: "))
            numbers.append (numberToAdd)

            for everynumber in numbers:
                print (f"{everynumber} + ")


            if not self.more ():
                break

    def multiply (self):
        while True:
            numberToAdd = int(input("Enter number: "))
            numbers.append (numberToAdd)

            for everynumber in numbers:
                print (f"{everynumber} + ")


            if not self.more ():
                break

    def divide (self):
    while True:
        numberToAdd = int(input("Enter number: "))
        numbers.append (numberToAdd)

        for everynumber in numbers:
            print (f"{everynumber} + ")


        if not self.more ():
            break


    def operation (self):
        print ("GELOs FIRST CALCULATOR")

        for _ in ops:
            print (_)

        input_operations = input(str("Choose your operations:" ))


        if input_operations == 1:
            add ()

        elif input_operations == 2:
            subtract ()

        elif input_operations == 3:
            multiply ()

        elif input_operations == 4:
            divide ()

        else:
            print ("Invalid Input")




             

calculator = Calculator ()
calculator.add ()
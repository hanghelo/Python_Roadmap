def sayHello():
    print ("Hello")

sayHello()

#########################

def sayHello2(name):
    print ("Hello", name)

sayHello2("Gelo")

#########################

def sayHello3(name):
    print ("Hello", name)


input_name = str(input("What is your name? "))
sayHello3(input_name)

#########################
#With Multiple Parameters

def fullname (firstName, lastName):
    print ("Hello, " + firstName + " " + lastName)


input_firstname = str(input("Enter your first name: "))
input_lastname = str(input("Enter your last name: "))

fullname (input_firstname, input_lastname)

#########################

def add(num1, num2):
    return num1 + num2

add (5,3)

#########################

def isLegalage (age):
    if age >= 18:
        return "Legal"
    else:
        return "underage"

print (isLegalage(12))
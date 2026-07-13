myfname = "Gelo"
mylname = "Reyes"
print (myfname + " " + mylname)

######################################

firstname = input ("Enter your first name: ")
lastname = input ("Enter your last name: ")

print ("Hi, " + firstname + " " + lastname)

######################################

firstNumber = input("Enter first number: ")
secondNumber = input("Enter second number: ")

sum = firstNumber + secondNumber
print (sum)

#answer is 55 because python treated is as string

######################################

first_Number = int(input("Enter first number: "))
second_Number = int(input("Enter second number: "))

sum2 = first_Number + second_Number
difference = first_Number - second_Number
product = first_Number * second_Number
qoutient = first_Number / second_Number

print (
    str(first_Number) + " + " + str(second_Number) + " = " + str(sum2),
    str(first_Number) + " - " + str(second_Number) + " = " + str(difference),
    str(first_Number) + " x " + str(second_Number) + " = " + str(product),
    str(first_Number) + " / " + str(second_Number) + " = " + str(qoutient)
    )

print (str(first_Number) + " + " + str(second_Number) + " = " + str(sum2))
print (str(first_Number) + " - " + str(second_Number) + " = " + str(difference))
print (str(first_Number) + " x " + str(second_Number) + " = " + str(product))
print (str(first_Number) + " / " + str(second_Number) + " = " + str(qoutient))
 
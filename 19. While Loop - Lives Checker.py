fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Grapes",
    "Pineapple",
    "Strawberry",
    "Watermelon",
    "Papaya",
    "Kiwi"
]


i = 0

while i < len(fruits):
    print (fruits[i])
    i = i + 1




stud = []
starting_student_ID = 2026000001


while starting_student_ID < 2026000101:
    print (starting_student_ID)
    stud.append(starting_student_ID)
    starting_student_ID = starting_student_ID + 1

print (stud)


i = 0

while i < 101:
    print ("I love you, Karen")
    i = i + 1


########################################################
lives = 3

while lives > 0:
    try:
        print ("1+1")
        user_answer = int(input("Enter your answer: "))
        correct_answer = 2
        if user_answer == correct_answer:
            print ("You are correct")
            break
        else:
            print ("Sorry. Try again")
            lives = lives - 1
            print ("You only have" , lives , "lives reamining")

    except ValueError:
        print ("Invalid input")
        lives = lives - 1
        print ("You only have" , lives , "lives reamining")

else:
    print ("Game over")
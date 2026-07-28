questions = [
    "1. What is the capital of the Philippines?",
    "2. Which planet is known as the Red Planet?",
    "3. What is the largest ocean on Earth?",
    "4. Which animal is known as the King of the Jungle?",
    "5. How many days are there in a leap year?",
    "6. Which programming language is this code written in?",
    "7. Which gas do plants absorb from the atmosphere?",
    "8. What is 15 + 20?",
    "9. Which is the largest mammal?",
    "10. Which keyword is used to create a loop in Python?"
]

options = [
    ["A. Cebu", "B. Davao", "C. Manila", "D. Baguio"],
    ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    ["A. Atlantic Ocean", "B. Arctic Ocean", "C. Indian Ocean", "D. Pacific Ocean"],
    ["A. Tiger", "B. Elephant", "C. Lion", "D. Bear"],
    ["A. 365", "B. 366", "C. 364", "D. 367"],
    ["A. Java", "B. Python", "C. C++", "D. JavaScript"],
    ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
    ["A. 30", "B. 35", "C. 40", "D. 45"],
    ["A. Elephant", "B. Giraffe", "C. Blue Whale", "D. Shark"],
    ["A. repeat", "B. loop", "C. while", "D. iterate"]
]

answers = [
    "C",
    "B",
    "D",
    "C",
    "B",
    "B",
    "C",
    "B",
    "C",
    "C"
]

lives = 3
score = []
print ("This is a quiz bee")

while lives > 0:

    i = 0
    while i < len(questions):
        print (questions[i])
        print ("Choices:", options[i])

        useranswer = str(input("Enter your answer: "))
        
        if (useranswer.lower() == answers[i].lower()):
            i = i + 1
            score.append(1)

        else:
            i = i + 1
            lives = lives - 1
            print ("Remaining lives, ", lives)

            if lives == 0:
                break

    else:
        print ("The quiz is over.")
        print ("Tallying your score.....")

        total = sum(score)
        print ("Your score is:", total)
        break


else:
    print ("Game Over")


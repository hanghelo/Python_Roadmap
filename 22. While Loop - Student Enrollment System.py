print ("===== Student Enrollment =====" \
"\n 1. Enroll Student" \
"\n 2. Remove Student" \
"\n 3. View Students " \
"\n 4. View Total Students" \
"\n 5. Exit")

useranswer_menu = int(input("Enter the menu number: "))
students = []
i = 0

while (useranswer_menu != 5):
    try:
        if (useranswer_menu == 1):
            print ("You are entering a Enrollment Menu ... ")
            print ("3 ... ")
            print ("2 ... ")
            print ("1 ... ")

            user_name = str(input("Enter your name: "))
            is_name_correct = str(input("Type [Y] for YES or [N] for NO: "))

            if (is_name_correct.lower() == "y"):
                students.append(user_name)
                print (user_name, "is now enrolled.")

                for student in students:
                    print ("Currently enrolled")
                break

            elif (is_name_correct == "n"):
                print ("Returning back to menu")

            else:
                print ("Only type Y or N next time")
                break


            #Break for the menu 1
            break

        elif (useranswer_menu == 2):
            try:
                to_remove = str(input("Enter the name of student to remove: "))
                students.remove(to_remove)
                print (to_remove,"is removed in the list")

            except ValueError:
                print ("Name not found")

            #Break for the menu 2
            break

        elif (useranswer_menu == 3):
            print ("Checking the list of student .....")

            if (len(students) < 0):
                print ("List of students", students)
                print (students.count())

                #break for the counting of students
                break

            else:
                print ("No enrolled students")

            #Break for menu #3
            break

        elif (useranswer_menu == 4):
            print ("The total students", len(students))

        else:
            print ("You have input a wrong menu number")
            #Break if wrong menu number
            break

    except ValueError:
        print ("Invalid input. You have entered a letter or a symbol. Please Try Again")

else:
    areyousure = str(input ("Are you sure? (Y/N)"))

    while (areyousure.lower == "y"):
        print ("How can i loop back?")

    else:
        print ("Thank you")

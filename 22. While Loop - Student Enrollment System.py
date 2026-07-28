students = []


while True:

    print ("===== Student Enrollment =====" \
            "\n 1. Enroll Student" \
            "\n 2. Remove Student" \
            "\n 3. View Students " \
            "\n 4. View Total Students" \
            "\n 5. Exit")

    useranswer_menu = int(input("Enter the menu number: "))

    try:
        if (useranswer_menu == 1):
            print ("You are entering a Enrollment Menu ... ")
            print ("3 ... ")
            print ("2 ... ")
            print ("1 ... ")

            while True:
                user_name = str(input("Enter your name: "))
                is_name_correct = str(input("Is the name correct?\nType [Y] for YES or [N] for NO: "))

                # Menu 1 - Kapag mag-eenter ng ieenroll
                if (is_name_correct.lower() == "y"):
                    students.append(user_name)
                    print (user_name, "is now enrolled.")
                    print ("Currently enrolled", students, "\n\n")

                    add_new_user = str(input("Do you want to add more? \nType [Y] for YES or [N] for NO: "))

                    if (add_new_user.lower() == "y"):
                        # Goes back to asking the name of the user
                        continue 

                    elif (add_new_user.lower() == "n"):
                        print ("Returning back to the menu...")
                        break

                    else:
                        print ("Invalid input. \nReturning back to the menu...\nNothing is added")
                        break

                # Menu 1 - Handling if mag-rere-enter ng name or not
                else:
                    reenter_name = str(input("Do you want to re-enter? \nType [Y] for YES or [N] for NO: "))
                    if (reenter_name.lower() == "y"):
                        continue

                    elif (reenter_name.lower() == "n"):
                        print ("Returning back to the menu...")
                        break

                    else:
                        print ("Invalid input. \nReturning back to the menu...")
                        break
            else:
                break
                    

        elif (useranswer_menu == 2):
            print ("You are entering the Remove Student Menu ... ")
            print ("3 ... ")
            print ("2 ... ")
            print ("1 ... ")

            while True:
                try:
                    to_remove = str(input("Enter the student's name to remove: "))

                    if (len(students) > 0):
                        print ("Student", to_remove, "is being search in the enrolled list.")
                        students.remove(to_remove)
                        print (to_remove, "is removed from the list")

                        remove_again = str(input("Do you want to remove again? \nType [Y] for YES or [N] for NO: "))

                        if (remove_again.lower() == "y"):

                            continue

                        elif (remove_again.lower() == "n"):
                            print ("Returning back to the menu...")
                            break

                        else:
                            print ("Invalid input. \nReturning back to the menu...\nNothing is removed")
                            break

                    else:
                        print ("No students is enrolled")
                        print ("Returning back to the menu...")
                        break

                except ValueError:
                    print (to_remove, "is not in the list or you may have typed incorrectly")

                    retry_deleting = str(input("Do you want to re-try removing? \nType [Y] for YES or [N] for NO: "))
                    if (retry_deleting.lower() == "y"):
                        continue
                    
                    elif (retry_deleting.lower == "n"):
                        print ("Returning back to the menu...")
                        break

                    else:
                        print ("Invalid input. \nReturning back to the menu...\nNothing is removed")
                        break
            else:
                break 



        elif (useranswer_menu == 3):
            print ("You are entering the View Students Menu ... ")
            print ("3 ... ")
            print ("2 ... ")
            print ("1 ... ")

            if (len(students) > 0):
                print ("Here is the currently enrolled students", students, "\nReturning back to the menu...")

            else:
                print ("No enrolled students.\nReturning back to the menu...")
                break


        elif (useranswer_menu == 4):
            print ("You are entering Total Count Students Menu ... ")
            print ("3 ... ")
            print ("2 ... ")
            print ("1 ... ")

            
            if (len(students) > 0):
                print ("You have total of ", len(students), "\nReturning back to the menu...")
                
            else:
                print ("No enrolled students.\nReturning back to the menu...")
                break

        elif (useranswer_menu == 5):
            print ("Exiting the system ... ")
            print ("3 ... ")
            print ("2 ... ")
            print ("1 ... ")
            break
        else:
            print ("Invalid keyword. Returning to the menu...") 

    except ValueError:
        print ("Invalid keyword. Returning to the menu...")

else:
    print ("Thank you!")
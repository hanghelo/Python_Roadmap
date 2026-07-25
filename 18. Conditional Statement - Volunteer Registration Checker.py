#You're creating a program for a volunteer registration system.

# Requirements
# Ask the user for their age.
print ("This is a program for a volunteer registration system.")

parameters = (18,"y",13,"n") # i just tried to use tuple


try:
    # If the age is 18 or older:
    # Ask if they have a Valid ID (yes or no).
    age = int(input("Enter your age: "))
    if age >= parameters[0]:

        # If they have a valid ID:
        print ("Do you have an ID? ")
        has_ID = str(input("Enter [Y] for YES and [N] for No: "))

        if has_ID.lower() == parameters[1]:
            print ("Registration Approved!")

        elif has_ID.lower() == parameters[3]:
            print ("Registration Denied. A valid ID is required.")

        else:
            print ("Registration Denied. You did not put a valid input. A valid input is required.")

    # If the age is 13 to 17:
    elif age >= parameters[2]:

        # Ask if they have Parent's Consent (yes or no).
        print ("Do you have your Parent's Consent? ")
        has_consent = str(input("Enter [Y] for YES and [N] for No: "))

        if has_consent.lower() == parameters[1]:
            print ("Registration Approved as a Youth Volunteer.")

        elif has_consent.lower() == parameters[3]:
            print ("Registration Denied. A parent's consent is required.")

        else:
            print ("Registration Denied. You did not put a valid input. A valid input is required.")

    # If the age is below 13:
    else:
        print ("Sorry, you are too young to register.")

except ValueError:
    print ("Sorry, you've entered an invalid input.")
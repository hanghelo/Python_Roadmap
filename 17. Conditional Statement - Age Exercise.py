#Age Checker
print ("This is an age checker")

try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print ("Age is", age, ". You are group to Adult Volunteer")

    elif age >=13:
        print ("Age is", age, ". You are group to Youth Volunteer")

    elif age >=10:
        print ("Age is", age, ". You are group to Child Volunteer")

    else:
        print ("Sorry you are underage. You cannot join the event now")

except ValueError:
    print ("Sorry, you have entered an invalid input. Please make that you enter a number.")
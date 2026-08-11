username = ["Gelo","Karen","Lorraine"]
password = ["123gelo","321karen","lukring"]

input_username = str(input("Enter your username: "))
input_password = str(input("Enter your password: "))


for x in range (len(username)):

    if input_username == username[x]:           #Checks if the input_username exists in the username list

        if input_password == password[x]:
            print ("Welcome ", username[x])
            break

        else:
            print ("Incorrect password")
            print ("Exiting the system ...")
            break



else:
    print ("Account not found")
    print ("Exiting the system ...")

print ("Thank you")
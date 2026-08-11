username = ["Gelo","Karen","Lorraine"]
password = ["123gelo","321karen","lukring"]

input_username = str(input("Enter your username: "))
input_password = str(input("Enter your password: "))


for x in range (len(username)):

    if input_username == username[x] and input_password == password [x]:
        print ("Welcome " + username[x])


else:
    print ("Account not found")
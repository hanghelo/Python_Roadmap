members = ["Gelo", "Karen", "Pia", "Ikang", "Wyne"]

def printingName (names):
    for name in names:
        print ("Hello,", name)

printingName(members)


print ("*****")

def printingName2 (*thenames):
    for eachname in thenames:
        print ("Hello,", eachname)

printingName2 ("Gelo", "Karen", "Pia", "Ikang", "Wyne")

print ("*****")

def printFamily (*firstName, lastName):
    for names in firstName:
        print (names + " " + lastName)

printFamily ("Gelo", "Aan", "Pia", "Ikang", "Wyne", lastName = "Reyes")

print ("*****")

def printStudent (name):
    print (name)

printStudent ("SDPT")
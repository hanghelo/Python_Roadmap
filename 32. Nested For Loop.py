products = [
    "Rice",
    "Bread",
    "Milk",
    "Eggs",
    "Coffee"
]

for everyproduct in products:               # Select the everyproduct in product list
    for everyletter in everyproduct:        # Select the everyletter in everyproduct
        print (everyletter, end="-")        # The end is use to put a separator to everyletter
    print ()                                # The print () is used to put and print new line


for x in range(5):                          # prints the x 5x (x = how many groups)
    for y in range (5):                     # prints the y 5x again (y = how many * inside each group)              
        print ("*")                         # prints * once for each y
    print ()                                # prints new line and groups the * by 5 vertically


for x in range(5):                          # print how many groups
    for y in range (10):                    # print how many * inside each group
        print ("*",end="-")                 # print * once for each y and "end" serve as the separator
    print ()                                # print new line


products = [
    ["Rice", 55],
    ["Bread", 45],
    ["Milk", 120],
    ["Eggs", 8],
    ["Coffee", 180]
]


for everyproductandprice in products:
    for everyitem in everyproductandprice:
        print (everyitem)
    print ()




students = [["BSIT",["David","Alenere"]],["BSCS",["Jaymar","Emman","Patrick"]]]

for student in students:
    print (student[0])
    for name in student[1]:
        print ("- ", name)
    print ()                                    #Everytime na matatapos sa new course, add new line
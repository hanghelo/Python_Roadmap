fruits = [
    "apple",
    "banana",
    "orange",
    "mango",
    "grape",
    "watermelon",
    "pineapple",
    "strawberry",
    "blueberry",
    "kiwi",
    "papaya",
    "avocado",
    "coconut",
    "peach",
    "pear"
]


for x in fruits:
    if x == "banana":
        print (x,"Bananaaaaa")
        break

    elif x =="apple":
        print (x,"An apple a day keeps the doctor away")


    else:
        print(x)



numbers = [1,2,3,4,5,6,7,8,9,10]


for x in numbers:
    if (x % 2) == 0:
        print (x,"is an even number")

    else:
        print (x)


for x in range (10):
    print (x)

for x in range(5):
    x = x+1
    print (x, ". Hello World")
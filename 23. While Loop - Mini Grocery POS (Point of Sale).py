inventory = [
    "Rice",
    "Bread",
    "Milk",
    "Eggs",
    "Coffee"
]

prices = [
    55,
    45,
    120,
    8,
    180
]

cart = []
cart_prices = []

sold_items = set()


# Display products one by one.
# Use a while loop, not for.

i = 0
print ("Current Inventory")
while (i < len(inventory)):
    print (inventory[i])
    i = i + 1


asked_product = str(input("Which product? "))

try:
    if asked_product.title() in inventory:
        while True:
            todo = str(input("What do you want to do? "))
            print ("""[A] Add to Card \n []""")




except ValueError:
    print ("Invalid Input")
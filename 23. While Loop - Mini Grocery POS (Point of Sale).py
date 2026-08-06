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

shop = str(input("Shop now? "))
try:
    if shop.lower() == "y":
        print ("Entering the shop")

        while True:
            # Display products one by one.
            # Use a while loop, not for.

            i = 0
            print ("Current Inventory")
            while (i < len(inventory)):
                print (inventory[i])
                i = i + 1


            asked_product = str(input("Which product? "))
            asked_product = asked_product.title()

            try:
                if asked_product in inventory:

                    # Getting the Item
                    cart.append(asked_product)
                    print ("Currently on cart", cart)

                    # Getting the Price
                    index_asked_product = inventory.index(asked_product)
                    cart_prices.append(prices[index_asked_product])
                    print ("Item", asked_product, "costs" , cart_prices)

                    # Remove from inventory
                    inventory.remove(asked_product)
                    sold_items.add(asked_product)

                    prices.pop(index_asked_product) #uses pop so when there is a duplicate or same price then the index will be the targetted to delete
                    print ("Sold items", sold_items)

                    # Current Total
                    total = sum(cart_prices)
                    print ("The total is ", total)


                else:
                    print ("Item Not Found")

                    searchagain = str(input("Do you want to search an item again? \nEnter [Y] Yess , [N] No: "))

                    if searchagain.lower() == "y":
                        continue
                    elif searchagain.lower () == "n":
                        print ("Exiting the system ...")
                        break
                    else:
                        print ("Invalid Input\nExiting the system")
                        break
            except ValueError:
                print ("Invalid Input\nExiting the system")
                break
                
        else:
            print("Thank you!")

    elif shop.lower() == "n":
        print ("Thank you!")

    else:
        print ("Thank you!")
except ValueError:
    print ("hey")
products = [
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


while True:
    print ("""===== CONVENIENCE STORE =====
    1. View Products
    2. Add to Cart
    3. View Cart
    4. Checkout
    5. Exit""")


    try:
        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            print ("Please see inventory items below:")
            for everyproduct in products:
                print("- " + everyproduct)
            print ("All inventory items are printed")

        elif user_choice == 2:
            print ("Entering Add to Cart")
            tobuy = str(input("Which product do you want to buy? "))
            propertobuy = tobuy.title()

            print ("Searching for " + propertobuy +" ...")

            if propertobuy in products:
                print (propertobuy + " is available")
                print ("Adding to Cart ...")

                #Adding to Cart
                cart.append(propertobuy)
                print ("Your current Cart: ", cart)

                #Getting the Index of the Item
                index_propertobuy = products.index(propertobuy)
                value_propertobuy = prices[index_propertobuy]
                cart_prices.append(value_propertobuy)

                print ("Current cart amount: ", sum(cart_prices))

                #Removing to Cart and the prices
                products.remove(propertobuy)
                prices.pop(index_propertobuy)

                #Printing other Available Product to upsell
                print ("\nOther Available Product")
                print(products)

            else:
                print (propertobuy + " is NOT available")

                wanttocontinue = str(input("Exit? Type YES[Y] or NO[N] :"))

                if wanttocontinue.upper() == "Y":
                    print ("Returning back to the menu ...")
                    continue

                elif wanttocontinue.upper() == "N":
                    print ("Exiting the system")
                    print ("Thank you!")
                    break

                else:
                    print ("Returning back to the menu ...")
                    continue               



        elif user_choice == 3:
            print (3)

        elif user_choice == 4:
            print (4)

        elif user_choice == 5:
            print (5)

        else:
            print (user_choice + " is not in the options")

    except ValueError:
        print ("You have entered an invalid input")

        wanttocontinue = str(input("Exit? Type YES[Y] or NO[N] :"))

        if wanttocontinue.upper() == "Y":
            print ("Returning back to the menu ...")
            continue

        elif wanttocontinue.upper() == "N":
            print ("Exiting the system")
            print ("Thank you!")
            break

        else:
            print ("Returning back to the menu ...")
            continue

    




# 2. Grocery Receipt Calculator ⭐⭐⭐

# This is related to your POS project, but now you must use for.

# Start with:

cart = ["Rice", "Milk", "Coffee", "Bread"]

prices = [55, 120, 180, 45]
# Your task

# Use a for loop to display:
print ("===== RECEIPT =====")
for item in range (len(cart)):
    print (cart[item], " - ", prices [item])    

# Total Items: 4
print ("Total Items: ", len(cart))

# Total Cost: 400
total = 0
for price in prices:
    total = total + price
    print (total)

    

# Bonus
# Use a loop to find the most expensive item.
# index_for_expensive = prices.index(max(prices))
# print ("Most expensive item: ", cart [index_for_expensive])
# print ("Item Price: ", index_for_expensive)

highest_price = 0
for price in prices:

    if price > highest_price:
        highest_price = price

index_of_the_highest_price = prices.index(highest_price)
print ("The most expensive item is: ", cart[index_of_the_highest_price])
print ("The most expensive price is: ", prices[index_of_the_highest_price])

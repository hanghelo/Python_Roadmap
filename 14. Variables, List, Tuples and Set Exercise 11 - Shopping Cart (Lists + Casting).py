# Exercise 11 - Shopping Cart (Lists + Casting) ⭐⭐⭐⭐

# Ask
# Enter item:
asked_item = str(input("Enter Item 1: "))

# Ask
# Enter price:
item_price = float(input("Enter price: "))

# Store both in separate lists.
items = []
items.append(asked_item)
print (items)

price = []
price.append(item_price)
print (price)

# Repeat three times (manually for now).
# 2nd
asked_item = str(input("Enter Item 2: "))
item_price = float(input("Enter price: "))
items.append(asked_item)
price.append(item_price)

asked_item = str(input("Enter Item 3: "))
item_price = float(input("Enter price: "))
items.append(asked_item)
price.append(item_price)

asked_item = str(input("Enter Item 4: "))
item_price = float(input("Enter price: "))
items.append(asked_item)
price.append(item_price)

# Print
print ("Items: " , items)
print ("Prices: " , price)

# Display
# Total Items:
print ("Total Items:" , len(items))

# Display
# Total Cost:
total_cost = price[0] + price[1] + price[2] + price[3]
print (total_cost)

# You need casting because input() returns strings.
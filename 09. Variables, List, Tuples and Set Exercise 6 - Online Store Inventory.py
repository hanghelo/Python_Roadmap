# Exercise 6 - Online Store Inventory ⭐⭐⭐
inventory = [
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor"
]

# User chooses
# Sold Item:
name = str(input("May I know what is your name? "))
print ("Hi ", name, "!")
sold_item = str(input("May I know what has just been sold? "))

# Remove it.
print ("Since it was just sold, I will be removing the item ", sold_item, " in the inventory list")
print ("Removing.............................")
inventory.remove(sold_item)

print ("Sorting.............................")
inventory.sort()
print ("Your updated inventory is as follows, sorted from A-Z ,", inventory)



# User enters
# New Stock:
new_stock = str(input("May I know the new stock that just arrived? "))

# Append it.
print ("Since it just arrived, I will be adding the item ", sold_item, " in the inventory list")
print ("Adding.............................")
inventory.append(new_stock)

print ("Sorting.............................")
inventory.sort()
print ("Your updated inventory is as follows, sorted from A-Z ,", inventory)

# Display inventory count.
print ("The total inventory items are ", len(inventory))

# Display the inventory sorted.
print ("Your updated inventory is as follows, sorted from A-Z ,", inventory)
# Mini Inventory Management System

# You're the inventory staff of a small computer shop.

# Start with:
inventory = [
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Webcam"
]

inv_backup = inventory.copy()
sold_items = set()


# Your program should:
# Display the current inventory.
print ("Current inventory: ", inventory)

# Ask the user which item was sold.
sold = str(input("Which item was sold? "))

# If the item exists in the inventory:
try:
    # Remove it from the inventory.
    inventory.remove(sold)
    print ("Item", sold, "is removed")
    print ("Current inventory: ", inventory)

    # Add it to sold_items.
    # Bakit nasa loob ng try and except? Dahil kapag nasa loob ng try-except, properly magwowork yung if-meron-o-wala na kondisyon. Kapag meron, duon lang niya iadd sa sold_item set
    # Now meron or wala yung item sa list, kapag nasa labas ito ng try-except, i-aadd at i-aadd pa rin niya.
    sold_items.add(sold)

except ValueError:
    print ("Item not found in the inventory")
    print ("Nothing is removed")

# Ask the user for a new stock item and add it to the inventory.
print ("Are there new stock?")
answer = str(input("Press (Y) for Yes or (N) for No:"))


if answer.lower() == "y":
    stock_to_add = str(input("Please enter the new item:"))
    inventory.append(stock_to_add)
    print (stock_to_add ,"is added in the list")
    print ("Your new inventory is as follows ,", inventory)

elif answer.lower() == "n":
    print ("Okay, nothing changed.")

else:
    print ("Invalid input. Please enter Y or N.")  


# Sort the inventory alphabetically.
inventory.sort()

# Display:
# Current inventory
print ("The current inventory list is as follows", inventory)

# Total number of inventory items
print("Total number of inventory items", len(inventory))

# Sold items
print("Sold items" , sold_items)

# Create a backup copy of the inventory.
# Binack up ko yung original list
# Kaya ko inilagay yung back up sa umpisa para sa umpisa pa lang ay may back up ako ng original list bago gawin ang changes

# Pero kung yung current inventory ang ibaback up, nasa ibaba ang pagback up ng current inventory
current_inventory_backup = inventory.copy()

# Show the difference between the backup and the sold items (which items remain unsold).
current_inventory_backup = set(current_inventory_backup)
remain_unsold = current_inventory_backup.difference(sold_items)
print ("Remain unsold", remain_unsold)
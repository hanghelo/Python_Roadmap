# Exercise 1 - Grocery Shopping List Manager ⭐ (Very Easy)
# Scenario
# You're about to go to the grocery store.
# Your program should help manage your shopping list.
# Requirements
# Start with
shopping_list = [ "Eggs", "Bread", "Milk"]

# Ask the user
# What item do you want to buy?
name = str(input("Hi, what is your name? "))
to_buy = str(input("What item do you want to buy? "))

# Add it to the list.
shopping_list.append(to_buy)

# Print the updated list.
print ("Your cart has ", shopping_list)

# Then ask
# What item have you already bought?
already_bought = str(input("What item have you already bought? "))

# Remove it.
shopping_list.remove(already_bought)

# Print the updated list again.
print ("You have removed ", already_bought)


# Finally
# Sort the list alphabetically.
shopping_list.sort()
print ("Your card is arranged from A-Z ", shopping_list)

# Reverse it.
shopping_list.sort(reverse=True)

# Print the final result.
print ("Your card is arranged from Z-A ", shopping_list)
print ("Congratulation you made it ", name)
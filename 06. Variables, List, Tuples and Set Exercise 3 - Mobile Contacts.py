# Exercise 3 - Mobile Contacts ⭐⭐

# Imagine you're creating the Contacts app.

# Start
contacts = [
    "Mom",
    "Dad",
    "Boss"
]

# Allow the user to
# Add one contact
addContact = str(input("Enter new contact: "))
contacts.append(addContact)

# Delete one contact
to_delete = int(input("Enter index to delete: "))
print ("Index ", to_delete, ", ", contacts[to_delete], " is being removed...")
print ("Index ", to_delete, ", ", contacts[to_delete], " is removed.")
contacts.remove(contacts[to_delete])
print ("The updated list is, ", contacts)

# Search by index
to_search = int(input("Enter index to search: "))
print ("Index ", to_search," is ", contacts[to_search])


# Example

# Enter index:

# Output

# Boss

# If the index doesn't exist

# Invalid contact.
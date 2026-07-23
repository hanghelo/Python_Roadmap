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
print ("This is your currenct contact list: ", contacts)
addContact = str(input("Enter new contact: "))
contacts.append(addContact)
contacts.sort()
print (addContact, " is added in the list,")
print ("You updated contact is as follows, sorted from A-Z ", contacts)

# Delete one contact
to_delete = int(input("Enter index to delete: "))
print ("Index ", to_delete, ", ", contacts[to_delete], " is being removed...")
print ("Index ", to_delete, ", ", contacts[to_delete], " is removed.")
contacts.remove(contacts[to_delete])
print ("The updated list is, ", contacts)

#Deleting through Keyword
anotherdelete = str(input("Enter the contact's name to delete: "))
contacts.remove(anotherdelete)
print (anotherdelete, " is being deleted from the list")
print ("deleting in 3.....")
print ("deleting in 2.....")
print ("deleting in 1.....")
print (anotherdelete, " is deleted from the contacts. And your updated contact is as follows, ", contacts)

# Search by index
to_search = int(input("Enter index to search: "))
print ("Index ", to_search," is ", contacts[to_search])


# Example

# Enter index:

# Output

# Boss

# If the index doesn't exist

# Invalid contact.
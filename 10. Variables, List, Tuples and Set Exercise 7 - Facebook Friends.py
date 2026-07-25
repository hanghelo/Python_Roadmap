# Imagine Facebook.

# You have
friends = [
    "Anna",
    "Ben",
    "Carlo"
]

backup = friends.copy() #Just to back up the list, so I copy it

# User can
# Add friend
add_friend = str(input("Enter the name of friend you want to add: "))
friends.append(add_friend)
friends.sort()
print (add_friend, " is added")
print ("This is your updated list of friends in alphabetical order: " , friends)

# Unfriend someone
unfriend = str(input("Enter the name that you want to unfriend: "))
friends.remove(unfriend)
friends.sort()
print (unfriend, " is removed")
print ("This is your updated list of friends in alphabetical order: " , friends)

# See total friends
print ("Total friend you have added is: " , len(friends))

# Extra
# Copy the friends list before making changes as a backup.
print (backup)
courses = ["BSIT","BSCS","BSIS","BSIE","BSEE"]
print (courses)

print (courses[2])
#answer: BSIS


########################
# Printing selected index
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "watermelon", "apricot", "apricot", "apricot"]

print (fruits [5:]) #will start printing index 5 up to the end
print (fruits [:5]) #will start printing index 0 up to the index 4 and index 5 is excluded
print (fruits [1:5]) #will start printing index 1 up to index 4 and index 5 is excluded

# writing or changing the value of a index
fruits [0] = "apricot"
print (fruits [0])
print (fruits)

# Identifying the length of a list
print (len (courses))

# Counting the number of occurence of an item in a list
print (fruits.count("apricot"))

# Adding item at the end of a list using APPEND
fruits.append ("cantaloupe")
print (fruits)

# Adding item at the SPECIFIC INDEX of a list using index
fruits.insert (1, "melon")
print (fruits)

# Removing item from list through KEYWORD using REMOVE 
fruits.remove ("melon")
print (fruits)

# Removing the last item using POP
fruits.pop ()
print (fruits)

# Removing a specific item through INDEX using pop
fruits.pop (1)
print (fruits)

# Deleting based on index but if index is not specified, it deletes the whole list
# del fruits [0]  # Deletes only the index 0
# del fruits      # Deletes the entire list since index is not defined
# print (fruits)

# Clearing all the items from a list
# fruits.clear () # Wala talaga siyang argument o inilalagay sa loob ng open and close parenthesis
# print (fruits)

# Copying a list
tosell = fruits.copy ()  # Wala talaga siyang argument o inilalagay sa loob ng open and close parenthesis
print ("tosell = " + str(tosell))

# Combining Lists
# 1st way using + sign
street_foods_1 = [
    "Kwek-kwek",
    "Fish Ball",
    "Isaw",
    "Kikiam",
    "Banana Cue"
]

street_foods_2 = [
    "Betamax",
    "Adidas",
    "Proben",
    "Turon",
    "Balut"
]

street_foods = street_foods_1 + street_foods_2
print (street_foods)

# 2nd way using extend
street_foods_1.extend(street_foods_2)
print ("The new extended list is: ", street_foods_1)


# 3rd way using append (Ginagamit for nested lsit)
street_foods_1.append(street_foods_2)
print ("The appended list is: ", street_foods_1)
# Create a list containing
# 5 favorite movies.
movies = [
    "A Walk to Remember",
    "Titanic",
    "Jurrasic Park",
    "Moulin Rouge",
    "Jumanji"
]

# Print
# Your first favorite movie is...
print ("Your first favorite movie is ", movies[0])

# Print
# Your last favorite movie is...
print ("Your last favorite movie is", movies[len(movies)-1])

# Replace one movie.
replacemovie = str(input("What another movie do you like? "))

print ("We are about to replace one of the movie on the list...")
print ("[1] ", movies[0])
print ("[2] ", movies[1])
print ("[3] ", movies[2])
print ("[4] ", movies[3])


movieindex = int(input("What movie do you want to replace? ")) - 1 #Nilagyan ng -1 para properly ma-hit yung index
print ("Enter the number of your choice:")

oldmovie = movies[movieindex] #Isinasave ko muna yung old muna

movies[movieindex] = replacemovie #Inaassign ko na yung new movie na papalit sa old movie
print ("The movie list is being updated in ...")
print ("3 ...")
print ("2 ...")
print ("1 ...")

print (replacemovie, " has replaced ", oldmovie)
print ("The updated movies are, ", movies)


# Sort.
movies.sort()
print ("Sorting movies in alphabetical A-Z order ...")
print ("Movies sorted in alphabetical A-Z order ")
print (movies)

# Reverse.
movies.sort(reverse=True)
print ("Sorting movies in alphabetical Z-A order ...")
print ("Movies sorted in alphabetical Z-A order ")
print (movies)

# Copy the list into another variable.
moviescopy = movies.copy()
print ("moviescopy", moviescopy)

# Delete the original list.
del movies


# Print only the copied list.
print ("moviescopy", moviescopy)
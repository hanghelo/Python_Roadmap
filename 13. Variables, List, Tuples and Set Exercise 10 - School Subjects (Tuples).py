# Exercise 10 - School Subjects (Tuples) ⭐⭐

# A student's schedule never changes.

# Store

# Math
# English
# Science
# History
# PE

# inside a tuple.
subjects = ("Math", "English", "Science", "History", "PE")

# Ask
# Which subject number do you want to view?
print("Which subject number do you want to view?:")
print ("Subjects")
print ("[0]     Math")
print ("[1]     English")
print ("[2]     Science")
print ("[3]     History")
print ("[4]     PE")
to_view = int(input("Enter the number code of the subject? "))

# Display it.
print ("The subject you are currently viewing is ", subjects[to_view])

# Display total number of subjects.
print ("Total number of subjects: " , len(subjects))

# Print first and last subject.
print ("The first subject is ", subjects[0])
print ("The last subject is ", subjects[len(subjects)-1])
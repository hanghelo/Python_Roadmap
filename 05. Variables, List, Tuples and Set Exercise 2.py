#Exercise 2 - Student Attendance Tracker ⭐⭐
#Scenario

#You're a teacher.
#Students arrive one by one.
# Start with

students = [
    "John",
    "Anna",
    "Mike"
]

# Ask for another student name.
print ("Hi Teacher!")
new_student = str(input("Enter the name of student that just arrived: "))

# Add it.
students.append(new_student)

# Display
print ("students")
# There are now 4 students.

# Ask
# Who is absent?
absent = str(input("Who is absent? "))

# Remove that student.
students.remove (absent)
print (absent, "is absent.")
print (absent, "is being removed from the list...")

# Display the final list.
print ("The final student's attendance is, ", students)

# Extra challenge:

# Print
# Student #1:
print ("Attendance:")
print (students[0]," is present")
# Student #2:
print (students[1]," is present")
# Student #3:
print (students[2]," is present")
# using indexes.
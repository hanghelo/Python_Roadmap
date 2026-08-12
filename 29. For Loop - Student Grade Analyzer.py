# 3. Student Grade Analyzer ⭐⭐⭐⭐

# Now let's make it more realistic.

students = [
    "John",
    "Anna",
    "Mike",
    "Sarah",
    "Kevin"
]

grades = [
    85,
    92,
    67,
    74,
    95
]

# The index represents the same student:

# John  → 85
# Anna  → 92
# Mike  → 67
# Sarah → 74
# Kevin → 95
# Your task

# Use a for loop to display:
for student_index in range (len(students)):

    if grades[student_index] > 75:
        print (students[student_index] , " - " , grades[student_index] , " - " , "Passed")

    else:
        print (students[student_index] , " - " , grades[student_index] , " - " , "Failed")

# Assume:

# 75 = Passing
# Then calculate:

# Total students
totalstudents = []
for everystudent in students:
    totalstudents.append(everystudent)
print ("The total student is: ", len(totalstudents)) # I just creat a new list so i can use for loop

#Other way is to create a variable
total_student_other_way = 0
for eachstudent in students:
    total_student_other_way = total_student_other_way + 1

print ("The total student is: ", total_student_other_way)



passed_count = 0
failed_count = 0
for student_remarks in grades:
    if student_remarks >= 75:
        passed_count = passed_count + 1

    else:
        failed_count = failed_count + 1

# Number passed
print ("Total passed: " , passed_count)

# Number failed
print ("Total failed: " , failed_count)



student_average = 0
student_highestgrade = 0
student_lowergrade = 100
grade_count = 0

for every_grade in grades:
    #for Average grade
    student_average = student_average + every_grade

    grade_count = grade_count + 1

    if every_grade > student_highestgrade:
        student_highestgrade = every_grade

    if every_grade < student_lowergrade:
        student_lowergrade = every_grade


# Average grade
averagegrade = student_average / grade_count
print ("Average grade: ", averagegrade)

# Highest grade
print ("Highest grade: ", student_highestgrade)

# Lowest grade
print ("Lowest grade: ", student_lowergrade)



# Bonus
# Find the student with the highest grade.
highest_student_grade = 0
for student_grade in grades:
    if student_grade > highest_student_grade:
        highest_student_grade = student_grade

student_name_with_highest_grade = grades.index(highest_student_grade)

print ("Top student: ", students[student_name_with_highest_grade])
print ("Grade: ", grades[student_name_with_highest_grade])

# 1. Employee Attendance Checker ⭐⭐
# Scenario

# You're helping HR check employee attendance for the week.

# Start with:

employees = ["John", "Anna", "Mike", "Sarah", "Kevin"]
absent = {"Mike", "Kevin"}

present = []

# Display every employee.
for employee in employees:

    if employee in absent:
        print (employees , "- Absent")

    else:
        print (employees , "- Present")
        present.append(employee)


# Count how many employees are present.
print ("Count of present employees, ", len(present))

# Count how many are absent.
print ("Count of absent employees, ", len(absent))

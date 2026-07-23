# Start
employees = [
    "John",
    "Maria",
    "Kevin",
    "Sarah"
]

# Ask
# Who resigned?
employees.sort()
print (employees)
resignedEmployee = str(input("These are your current employees, but may I know who has just resigned? "))

# Remove.
employees.remove(resignedEmployee)
print ("Thanks for answering")
print ("I will be removing ", resignedEmployee, " in the masterlist.")
print ("The list is already updated. The updated list is as follows ,", employees)

# Ask
# Who got hired?
recentlyHired = str(input("May I know who has just recently hired? "))

# Append.
employees.append(recentlyHired)
print ("Thanks for answering")
print ("I will be adding ", recentlyHired , " in the masterlist.")
print ("The list is already updated. The updated list is as follows ,", employees)


# Finally display
# Total employees:
print ("The current total employees is ",len(employees) , "sorted from A-Z below")

# Sort alphabetically.
employees.sort()
print (employees)
# Exercise 12 - Gym Attendance (Sets) ⭐⭐⭐⭐

# Monday attendees
Monday_attendees = {
    "John",
    "Anna",
    "Mike",
    "Kevin"
    }

# Tuesday attendees
Tuesday_attendees = {
    "Anna",
    "Kevin",
    "Rose,"
    "Carl"
    }

# Find
# People who came both days.
came_both_days = Monday_attendees.intersection(Tuesday_attendees)
print ("The people who came both days are", came_both_days)

# People who only came Monday.
monday_only = Monday_attendees.difference(Tuesday_attendees)
print ("People who only came Monday" , monday_only)

# People who only came Tuesday.
tuesday_only = Tuesday_attendees.difference(Monday_attendees)
print ("People who only came Tuesday" , tuesday_only)

# People who attended at least one day.
atleast_oneday = Monday_attendees.union(Tuesday_attendees)
print ("People who attended at least one day.", atleast_oneday)
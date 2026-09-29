student = {
    "name": "Juan Dela Cruz",
    "age": 20,
    "gender": "Male",
    "student_id": "2026-001",
    "course": "BS Information Technology",
    "year_level": 2,
    "section": "IT-2A",
    "email": "juan@email.com",
    "gpa": 1.75,
    "status": "Active"
}

#Add items
student["graduation_year"] = 2026
for key,value in student.items():
    print (f"{key}: {value}")

#Copy a dictionary
student2 = student.copy()
print ()
print ("Student 2")
for key,value in student2.items():
    print (f"{key}: {value}")

#Edit/Update
student["course"] = "BS IE"
print (f"Course: {student["course"]}")

#Read
print (student)             #print all what's inside the dictionary
print (student["age"])      #print a specific value of a dictionary using a key
print (student.get("age"))  #another way to print a specific value of a dictionary using a key

print (f"Length: {len(student)}")   #prints the number of keys/value entry

print (f"All keys of Student: \n{student.keys()}")        #prints all the keys
print (f"All values of Student: \n{student.values()}")    #prints all the keys

#Delete
student.pop("name")         #remove student name as key value pair
print (student)

student.popitem()           #remove the last key-value pair of a dictionary
print (student)

student2.clear()            #clears the entire dictionary
print (student2)
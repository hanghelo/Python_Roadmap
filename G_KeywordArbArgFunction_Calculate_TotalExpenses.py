name = "Gelo"
position = "Technical Product Manager"
department = "IT"
work_setup = "Remote"
experience = 5


def employee_profile(**empinfo):
    print ("Employee Profile")
    for key, value in empinfo.items():
        print (f"{key}: {value}")

employee_profile (Name = name, Position = position, Department = department, Work_Setup = work_setup, Experience = experience)
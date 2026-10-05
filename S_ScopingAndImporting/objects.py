class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce (self):
        print (f"""Name: {self.name}
                Course: {self.course}""")
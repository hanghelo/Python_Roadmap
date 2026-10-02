class Person:
    def __init__(self, name):
        self.name = name

    def introduce (self):
        print (f"Hi! I am {self.name}")


listOfPeople = []

for name in range(5):
    name = input(str("Name: "))
    personToCreate = Person (name)
    listOfPeople.append(personToCreate)

print (listOfPeople)
#Output: <__main__.Person object at 0x00000297E8E88590>, <__main__.Person object at 0x00000297E8E78550>, <__main__.Person object at 0x00000297E8E78690>


for everyname in listOfPeople:
    everyname.introduce()
class Animal:
    def __init__(self, type, voice):
        self.type = type
        self.voice = voice

    def speak (self):
        print (self.voice)
        print ("The animal is a" + self.type)
        print ()

dog = Animal ("Dog","Arf")
dog.speak()

cat = Animal ("Cat", "Meow")
cat.speak ()


class socialmedia:
    def __init__(self, firstName, lastName, likesCount, friendsName):
        self.firstName = firstName
        self.lastName = lastName
        self.likesCount = likesCount
        self.friendsName = friendsName
        print (f"User created name: {firstName}")

    def introduce (self):
        print (f"Hello! My name is {self.firstName} {self.lastName}")

    def fullprofile (self):
        print ("Full Profile:")
        print (f"Full Name: {self.firstName} {self.lastName}")
        print (f"Likes: {str(self.likesCount)}")
        print ("Friends:")
        for everyfriend in self.friendsName:
            print (f"- {everyfriend}")

gelo = socialmedia ("Gelo", "Reyes", 10, ["Karen", "Wyne", "LJ","Angel"])

gelo.introduce()
gelo.fullprofile()
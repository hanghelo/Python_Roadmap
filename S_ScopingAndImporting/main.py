# Global Variables
y = "World"         # Can be called  within the whole file


# Local Variables
def sayHello ():
    x = "Hello"     # Can only be called only to the block of called
    print (x)

sayHello ()


# Global Keyword
def say ():
    global y    # use to call global variable
    y = "Hello"
print (y)       # Local

# say (y)         # Local
print (y)       # Global

###################################3333
import arimethic
import constants
import objects

print (arimethic.add (5,2))
print (constants.pi)

s1 = objects.Student("Davide","BSIE")
s1.introduce()





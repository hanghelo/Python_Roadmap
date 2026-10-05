

# Parent Class - Product
class Product ():

    # Attributes
    def __init__(self, name, code, quantity, price, category):
        self.name = name
        self.code = code
        self.quantity = quantity
        self.price = price
        self.category = category

    # Methods / Functions

###########################################################################################################
# Child Class - Product Category

class MedicineItem (Product):
    def __init__(self, name, code, quantity, price, category, manufacturing_date, expiration_date, brand):
        super().__init__(name, code, quantity, price, category)

        #Additional Attribute for medicine items
        self.manufacturing_date = manufacturing_date
        self.expiration_date = expiration_date
        self.brand = brand

class ElectronicsItem (Product):
    def __init__(self, name, code, quantity, price, category, supporteddevice):
        super().__init__(name, code, quantity, price, category)

        #Additional Attribute for electronics items
        self.supporteddevice = supporteddevice


class FoodAndBevItem (Product):
    def __init__(self, name, code, quantity, price, category, bestbefore):
        super().__init__(name, code, quantity, price, category)

        #Additional Attribute for foodandbev items
        self.bestbefore = bestbefore


##############################
# Defininig Inventory Categories
inventoryCategory = ["Medicine Category", "Electornic Category", "Food and Beverages "]

def invCat (inventoryCategory):
    for i, category in enumerate(inventoryCategory):
        print (f"[{i+1}] - {category} ")


# Printing Inventory Items
inventory = []

def invItems (inventory):
    for i, inventoryItems in enumerate(inventory):
        print (f"[{i+1}] - {inventoryItems} ")

##############################
# Try Again
def tryAgain ():

    input_tryAgain = str(input("Try Again? Type [Y] for Yes or [N] for No: "))

    if input_tryAgain.upper() == "Y":
        return addInventory ()

    elif input_tryAgain.upper() == "N":
        return False

    else:
        print ("Invalid input")
        print ("Exiting the system ...")
        return False

################################



#1. Add 
def addInventory ():
    print (f"""Adding a new inventory item ...
            f"\nTo add new item, please type below the item category""")
    print ()

    #Print Inventory Category
    invCat (inventoryCategory)

    itemCategory = int(input("Enter category number: "))

    # Medicine
    if itemCategory == 1:
        # Common Atrib
        name = input("Item name: ")
        code = int(input("Item code: "))
        quantity = int(input("Item quantity: "))
        price = int(input("Item price: "))

        # Addtnl Attrib
        manufacturing_date = str(input("Item mfc date: "))
        expiration_date = str(input("Item exp date: "))
        brand = str(input("Item brand: "))

        medicine = MedicineItem (name, code, quantity, price, "Medicine", manufacturing_date, expiration_date, brand)

        inventory.append(medicine)
        print (f"{medicine.name} is created")


    # Electornics
    elif itemCategory == 2:
        # Common Atrib
        name = input("Item name: ")
        code = int(input("Item code: "))
        quantity = int(input("Item quantity: "))
        price = int(input("Item price: "))

        # Addtnl Attrib
        supporteddevice = input(str("Supported Device: "))

        electronics = ElectronicsItem (name, code, quantity, price, "Electronics",supporteddevice)

        inventory.append(electronics)
        print (f"{electronics.name} is created")

    elif itemCategory == 3:
        # Common Atrib
        name = input("Item name: ")
        code = int(input("Item code: "))
        quantity = int(input("Item quantity: "))
        price = int(input("Item price: "))

        # Addtnl Attrib
        bestbefore = input(str("Best before: "))

        foodandbev = FoodAndBevItem (name, code, quantity, price, "Food and Beverages", bestbefore)

        inventory.append(foodandbev)
        print (f"{foodandbev.name} is created")
    else:
        print ("Invalid Category!")

#2. Remove Inventory 
def removeInventory (inventory):
    print (f"""Removing a existing inventory item ...
            f"\nTo remove an item, please type below the item category""")
    print ()

    # Printing Categories
    invCat (inventoryCategory)

    # Asking what category
    itemCategory = int(input("Enter category number: "))
    print (f"Entering cateogry {itemCategory}")

    # Printing available items within the category

    

    # Accessing Category


    

    itemToRemove = str(input("Enter item name to remove: "))








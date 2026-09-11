evenNumbers = {2,4,6,8,10}
print (evenNumbers)

# Checkiong the Length of a Set
print ("Length is: ", len(evenNumbers))

# Adding an Item in a Set
evenNumbers.add("Gelo")
print (evenNumbers)

# Adding multiple items or a list in a set using update
# Manual declaration of items to add
evenNumbers.update([12,14,16])
print (evenNumbers)

additional_numbers = [18,20]
# Adding through a list
evenNumbers.update(additional_numbers)
print (evenNumbers)

#############################################################
#############################################################

# DELETING AN ITEM or ITEMS 

# REMOVE
# Removing or Deleting an Item using Remove
# Yung ireremove ay existing sa set
# Hindi siya mag-eerror dahil existing yung 2 na value sa set
evenNumbers.remove (2)
print (evenNumbers)

letters = {"a", "b", "c"}
letters.remove ("a")
print (letters)

# Yung ireremove ay wala sa set
# Mag-eerror dahil wala yung 1 na value sa set
# evenNumbers.remove (1)
# print (evenNumbers)
# Output: evenNumbers.remove (1)

# DISCARD
# Removing or Deleting an Item using DISCARD
# Ang difference ng Discard sa Remove ay, yung Discard walang error message kung hindi existing yung value
# Kumbaga si Remove may pakelam na i-alert ka, pero si Discard ay wala
evenNumbers.discard (1)
# Take note walang 1 sa set
print (evenNumbers)

# POP
# Remove yung first item sa set
evenNumbers.pop ()
evenNumbers.pop () # 2nd pop
print (evenNumbers)


# CLEAR
# Clearing yung laman ng set
# Buburahin yung items sa set pero yung SET container ay hindi mabubura
evenNumbers.clear ()

#############################################################
#############################################################

# COPYING a Set using COPY
fruits = {
    "apple",
    "banana",
    "orange",
    "grape",
    "mango",
    "pineapple",
    "watermelon",
    "strawberry",
    "kiwi",
    "peach"
}

fruitCopy = fruits.copy()
print (fruits)
print (fruitCopy)

#############################################################
#############################################################

# SET OPERATIONS
    # UNION - Combine a set and returns the unique values
    # DIFFERENCE - lahat ng meron si setOne na meron si setTwo ay matatanggal
    # SYMMETRIC DIFFERENCE - lahat ng walang kaparehas na value sa mga set, ay rereturn ng system. 2 sets lang ang pwede icompare using this.

unangSet = {"Karen", "Gelo", "Ikang"}
secondSet = {"Karen", "Wyne"}

#Union - returns unique values
thirdSet = unangSet.union(secondSet)
print (thirdSet)

#Difference
fourthSet = unangSet.difference(secondSet)
print (fourthSet)
#Output: {'Gelo', 'Ikang'} --- dahil nauna ang unangSet

fifthSet = secondSet.difference (unangSet)
print (fifthSet)

#Symmetric Difference - irereturn yung mga values na walang kaparehas, di imporntant yung order dito sa kung ano ang mauunang set dahil iipunin naman ng system yung walang mga kagaya na values. 2 sets lang ang pwede icompare using this.
sample_set_1 = {1,2,3,4,5,6,7,8,9,10}
sample_set_2 = {4,5,6,7}
sample_set_3 = {8,9,10,11,12,13,14,15}

sample_set_4 = sample_set_1.symmetric_difference (sample_set_2)
print (sample_set_4)
#Output: sample_set_4 = {1,2,3,11,12,13,14,15}


#Disjoint Set
# a function na nagchecheck kung may magkaparehas na value/item ang dalawang set.
# nagrereturn ng TRUE or FALSE. True kung may magkaparehas and FALSE kung wala.
# Hindi mahalaga ang ordering neto dahil both set ang cinocompare
print(sample_set_1.isdisjoint(sample_set_2))
# Output: FALSE

#Subset
# Yung set na maliit ay tinitignan kung siya ay nasa set na mas malaki.
# Small inside Big: ll the small box items are inside the big box.
numbers = {1,2,3,4,5,6,7,8,9,10}
even_Numbers = {2,4,6,8,10}

print(evenNumbers.issubset(numbers))
#Output: TRUE - dahil lahat ng numbers na 2,4,6,8,10 ay nageexist sa numbers set.
#Now if ang isang number mula sa even number ay hindi existing sa numbers, magfafalse na ito kaagad.

#Superset
#Big holds Small - the big box has all the small box items (and maybe more).
print(numbers.issuperset(even_Numbers))
#Output: TRUE - dahil yung numbers (superset) ay may value na kagaya sa even_Numbers (subset)
#Now if ang isang number mula sa even number ay hindi existing sa numbers, magfafalse na ito kaagad.

#Casting Set

#Set to List
numbers = list(numbers)
print ("This is a set, ", numbers)

#List to Tuples
numbers = tuple(numbers)
print ("This is a set, ", numbers)

#Tuples to Set
numbers = set(numbers)
print ("This is a set, ", numbers)
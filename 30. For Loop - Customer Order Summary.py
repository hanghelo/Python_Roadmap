customers = [
    "John",
    "Anna",
    "Mike",
    "Sarah",
    "John",
    "Mike"
]

orders = [
    "Burger",
    "Pizza",
    "Burger",
    "Pasta",
    "Pizza",
    "Burger"
]

prices = [
    120,
    180,
    120,
    150,
    180,
    120
]


for each_customer in range(len(customers)):
    print (str(customers[each_customer]) + " - " + str(orders[each_customer]) + " - " + str(prices[each_customer]))


######################################################
# Total Sales
# Most Expensive

total_sales = 0
most_expensive = 0

for each_purchase in prices:

    #for total_sales
    total_sales = total_sales + each_purchase

    #for most_expensive
    if each_purchase > most_expensive:
        most_expensive = each_purchase



    
    
print ("The total sales is ", total_sales)

index = prices.index(most_expensive)

print("Most expensive order:", customers[index], "-", orders[index], "-", prices[index])
######################################################
# Total Count
total_count = 0
for each_item in orders:
    total_count = total_count + 1

print ("The total count is ", total_count)
######################################################
customers_set = set(customers)

for each_buyer in customers_set:
    print (each_buyer, customers.count(each_buyer))

    
           
    # if each_buyer == "John":
    #     print (each_buyer, customers.count(each_buyer))

    # elif each_buyer == "Sarah":
    #     print (each_buyer, customers.count(each_buyer))

    # elif each_buyer == "Anna":
    #     print (each_buyer, customers.count(each_buyer))      

    # elif each_buyer == "Mike":
    #     print (each_buyer, customers.count(each_buyer))

    # else:
    #     print ("hey")    

# Unique customers
customers_set = list(customers_set)
customers_set.sort()

print ("Unique Customers:")
for every_unique_customer in customers_set:
    print ("- " , every_unique_customer)


# Ordered more than once.
for every_repeat_buyer in customers_set:

    if (customers.count(every_repeat_buyer)) > 1:
        print(every_repeat_buyer, customers.count(every_repeat_buyer))

    
    




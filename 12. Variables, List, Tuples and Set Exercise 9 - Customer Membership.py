# Store A members
StoreA_members = {
"John",
"Anna",
"Mike",
"Rose",
"Gelo",
"Karen"
}

# Store B members
StoreB_members = {
"Mike",
"Rose",
"Kevin",
"Jake",
"Gelo",
"Karen"
}

# Find

# VIP customers
# (Customers in both stores)
vip_customers = StoreA_members.intersection(StoreB_members)
vip_customers = list(vip_customers)
vip_customers.sort()

print ("Customers in both stores", vip_customers)

# Customers exclusive to each store.
exclusiveA = StoreA_members.difference(StoreB_members)
print ("Exclusive on Store A: ", exclusiveA)

exclusiveB = StoreB_members.difference(StoreA_members)
print ("Exclusive on Store B: ", exclusiveB)

# Total unique customers.
print ("Total unique customers: ", len(StoreA_members.union(StoreB_members)))
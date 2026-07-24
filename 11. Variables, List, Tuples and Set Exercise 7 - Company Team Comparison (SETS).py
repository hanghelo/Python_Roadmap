Department_A = {"John","Anna","Mike","Sarah"}
Department_B = {"Mike","Sarah","Kevin","Rose"}

# Find

# Everyone
Department_C = Department_A.union(Department_B)
print ("Everyone ," , Department_C)

# Common employees
common_employees = Department_A.intersection(Department_B)
print ("Common employees ," , common_employees)

# Employees only in A
print ("Employees only in A ," , Department_A.difference(Department_B))

# Employees only in B
print ("Employees only in B ," , Department_B.difference(Department_A))

# Employees not shared
not_shared = Department_A.symmetric_difference(Department_B)
print ("Employees not shared ," , not_shared)

# Are they disjoint?
print("Are they disjoint? " , Department_A.isdisjoint(Department_B))

# Is A subset of B?
print("Is A subset of B? ," , Department_B.issubset(Department_A))

# Is B superset of A?
print("Is B superset of A? ," , Department_B.issuperset(Department_A))


# Skills
# Every Set operation.
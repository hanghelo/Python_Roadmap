food = 150
transport = 80
groceries = 120
coffee = 50

def calculate_expenses(*expense_items):
    total = 0
    for x in expense_items:
        total = total + x
    return total


expense_total = calculate_expenses (food, transport, groceries, coffee)
print ("Total Expense: " , expense_total)
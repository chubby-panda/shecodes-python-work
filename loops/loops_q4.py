groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08],
]

total = 0

# Get quantity and add to total
for item in groceries:
    quantity = input(f"How many units of {item[0]} do you have? ")
    total += (item[1] * float(quantity))
    item.append(quantity)

print("====Izzy's Food Emporium====")
for item in groceries:
    item_total = f"${float(item[1]) * float(item[2]):.2f}"
    print(f"{item[0]:<20}{item_total:>8}")
print("============================")
total = f"${total:.2f}"
print(f"{total:>28}")
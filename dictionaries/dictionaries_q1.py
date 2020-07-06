# Create a list of grocery items for purchase
# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08],
# ]

groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08,
}

# Define a function to calculate the total cost of an item
def calculate_cost(unit_price, number_purchase):
    item_total = unit_price * float(number_purchase)
    return item_total

# Create a variable containing the total cost
total = 0

# Get quantity and add to total
for item, price in groceries.items():
    quantity = input(f"How many units of {item} do you have? ")
    groceries[item] = calculate_cost(price, quantity)
    total += groceries[item]

# Print Receipt
print("====Izzy's Food Emporium====")
for item, price in groceries.items():
    price = f"${price:.2f}"
    print(f"{item:<20}{price:>8}")
print("============================")
total = f"${total:.2f}"
print(f"{total:>28}")
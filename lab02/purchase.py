price = int(input("Enter price: "))

count = int(input("Enter count: "))

paid = int(input("Enter paid amount: "))

total_cost = price * count
change = paid - total_cost

print(f"Total cost: {total_cost} rub")
print(f"Change: {change} rub")
## Вариант 2 (Книжный магазин, Учебники, Сборники задач)

order_name = input("Enter order name: ")
customer_name = input("Enter customer name: ")

item1_name = input("Enter first item name: ")
item1_qty = int(input(f"Enter quantity for {item1_name}: "))
item1_price = float(input(f"Enter unit price for {item1_name}: "))

item2_name = input("Enter second item name: ")
item2_qty = int(input(f"Enter quantity for {item2_name}: "))
item2_price = float(input(f"Enter unit price for {item2_name}: "))

discount_percent = float(input("Enter discount percentage: "))

delivery_cost = float(input("Enter delivery cost: "))
amount_paid = float(input("Enter amount paid by customer: "))

item1_total = item1_qty * item1_price
item2_total = item2_qty * item2_price

total_items_cost_raw = item1_total + item2_total
discount_rub = total_items_cost_raw * (discount_percent / 100)
total_items_cost = total_items_cost_raw - discount_rub

grand_total = total_items_cost + delivery_cost
total_quantity = item1_qty + item2_qty
change = amount_paid - grand_total

print(f"Order: {order_name}")
print(f"Customer: {customer_name}")
print(f"{item1_name} | Qty: {item1_qty} | Price: {item1_price:.2f} | Total: {item1_total:.2f}")
print(f"{item2_name} | Qty: {item2_qty} | Price: {item2_price:.2f} | Total: {item2_total:.2f}")
print("-"*50)
print(f"Items initial cost:   {total_items_cost_raw:.2f} RUB")
print(f"Discount ({discount_percent}%):   {discount_rub:.2f} RUB")
print(f"Items net cost:       {total_items_cost:.2f} RUB")
print(f"Delivery cost:        {delivery_cost:.2f} RUB")
print(f"Grand total:          {grand_total:.2f} RUB")
print(f"Total units quantity: {total_quantity} pcs")
print("-"*50)
print(f"Amount paid:          {amount_paid:.2f} RUB")
print(f"Change to return:     {change:.2f} RUB")


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b == 0:
        print("Division by zero is undefined")
        exit()
    result = a / b
else:
    print("Unknown operation!!!!!")
    exit()

print(f"Result: {result:.2f}")

text = input("Enter numbers: ")

rowNumbers = text.split()

numbers = []
new_numbers = []

for rowNumber in rowNumbers:
    number = int(rowNumber)
    numbers.append(number)

for number in numbers:
    new_numbers.append(abs(number))

print(f"Original list: {numbers}")
print(f"New list: {new_numbers}")

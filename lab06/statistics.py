text = input("Enter numbers: ")

rowNumbers = text.split()

if len(rowNumbers) == 0:
    print("No data")
    exit()

numbers = []
total = 0
minimum = float('inf')
maximum = float('-inf')

for rowNumber in rowNumbers:
    number = int(rowNumber)
    total += number

    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number

    numbers.append(number)

print(f"Count: {len(numbers)}")
print(f"Sum: {total}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Average: {total / len(numbers):.2f}")

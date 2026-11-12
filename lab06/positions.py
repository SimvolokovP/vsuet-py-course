text = input("Enter numbers: ")

rowNumbers = text.split()

if len(rowNumbers) == 0:
    print("Нет данных")
    exit()

numbers = []

for rowNumber in rowNumbers:
    number = int(rowNumber)
    numbers.append(number)

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

positions = []

for i, number in enumerate(numbers):
    if number == maximum:
        positions.append(i)

print(f"Positions: {positions}")

## Вариант 2 (Отриц числа, [-8, -3], 2, -11)

text = input("Enter numbers: ")

rowNumbers = text.split()

numbers = []
selected_numbers = []

for rowNumber in rowNumbers:
    number = int(rowNumber)
    numbers.append(number)

for number in numbers:
    if number < 0:
        selected_numbers.append(number)

sorted_numbers = sorted(selected_numbers)

total = sum(selected_numbers)
count = len(selected_numbers)

print(f"Selected numbers: {selected_numbers}")
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Sorted numbers: {sorted_numbers}")

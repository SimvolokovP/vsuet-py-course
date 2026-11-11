## Вариант 2 (Отриц числа, 2, -15)

n = int(input("Enter n: "))

if n < 0:
    print("n cannot be negative.")
    exit()

count = 0
total = 0

for i in range(n):
    number = int(input("Enter number: "))

    if number < 0:
        count += 1
        total += number

print(f"Count: {count}")
print(f"Sum: {total}")
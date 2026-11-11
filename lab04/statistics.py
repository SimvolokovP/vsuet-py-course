n = int(input("Enter n: "))

if n < 1:
    print("n < 1")
    exit()

total = 0
positive_count = 0

for i in range(n):
    number = int(input("Enter number: "))

    total += number

    if number > 0:
        positive_count += 1

    if i == 0:
        maximum = number
    elif number > maximum:
        maximum = number

print(f"Sum: {total}")
print(f"Positive numbers: {positive_count}")
print(f"Maximum: {maximum}")

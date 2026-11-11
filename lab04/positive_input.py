rejected_attemptss = 0
number = int(input("Enter number: "))

while number <= 0:
    rejected_attemptss += 1
    number = int(input("Enter number: "))

print("Square:", number ** 2)
print("Rejected attempts:", rejected_attemptss)
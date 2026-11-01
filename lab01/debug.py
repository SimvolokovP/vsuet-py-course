## Fragment A

first = "2"
second = "3"
print(first + second)

## Fragment A corrected

number1 = "2"
number2 = "3"
## transform to int
print(int(number1) + int(number2))

## Fragment B

age = input("Age: ")
print(f"age: {type(age)}")
# print(age + 1) # This causes a TypeError

## Fragment B corrected

age_input = input("Age: ")
## transform to int
age = int(age_input)
print(f"age: {type(age)}")
print(f"age next year: {age + 1}")
print()

## Fragment C

first = 4
second = 7
third = 10
average = first + second + third / 3
print(f"Result: {average}")

## Fragment C corrected

first = 4
second = 7
third = 10
## add parentheses to fix operator precedence
average = (first + second + third) / 3
print(f"Corrected result: {average}")
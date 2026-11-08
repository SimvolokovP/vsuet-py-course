## Вариант 2 (Заполненность хранилища)

storage = int(input("Enter storage fullness (0-100): "))

if storage < 0 or storage > 100:
    print("Range error")
elif 0 <= storage <= 49:
    print("Free!")
elif 50 <= storage <= 89:
    print("Not enough space")
else:
    print("Almost full")

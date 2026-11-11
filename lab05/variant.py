## Вариант 2 (Заканчивается на я)

text = input("Enter text: ")

words = text.split()
count = 0

for word in words:
    word = word.strip(".,!?;:").lower()

    if word == "":
        continue

    if word.endswith("я"):
        print(word)
        count += 1

if count == 0:
    print("Нет совпадений")

print(f"Count: {count}")

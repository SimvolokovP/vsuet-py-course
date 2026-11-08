## Вариант 2 (Количество книг, Книг в коробке)

total = int(input("Enter number of books: "))

capacity = int(input("Enter books per box: "))

full_boxes = total // capacity
remaining_books = total % capacity
min_boxes = (total + capacity - 1) // capacity

print(f"Full boxes: {full_boxes}")
print(f"Remaining books: {remaining_books}")
print(f"Minimum boxes needed: {min_boxes}")

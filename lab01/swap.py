first_room = input("Enter first room: ")
second_room = input("Enter second room: ")

print(f"First room: {first_room}")
print(f"Second room: {second_room}")

temp = first_room
first_room = second_room
second_room = temp

print(f"First room after swap: {first_room}")
print(f"Second room after swap: {second_room}")
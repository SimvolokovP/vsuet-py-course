first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
group = input("Enter group: ")
city = input("Enter city: ")

age = int(input("Enter age: "))
    
hours_per_week = float(input("Enter preparation hours per week: "))

favorite_subject = input("Enter favorite subject: ")

full_name = f"{first_name} {last_name}"
age_in_4_years = age + 4
hours_in_4_weeks = hours_per_week * 4
hours_per_day = hours_per_week / 7

print(f"Student profile: {full_name}")
print(f"Group: {group}")
print(f"City: {city}")
print(f"Favorite subject: {favorite_subject}")
print(f"Age in 4 years: {age_in_4_years} y.o.")
print(f"Hours in 4 weeks: {hours_in_4_weeks:.2f} hrs")
print(f"Daily average hours: {hours_per_day:.2f} hrs")
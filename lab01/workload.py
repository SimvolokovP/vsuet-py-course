subject1 = input("Enter first subject name: ")
classes1 = int(input(f"Enter number of classes per week for {subject1}: "))
if classes1 < 0:
    print("value must be a positive number")
    exit()

duration1 = int(input(f"Enter duration of one class for {subject1}: "))
if duration1 <= 0:
    print("value must be a positive number")
    exit()

subject2 = input("Enter second subject name: ")
classes2 = int(input(f"Enter number of classes per week for {subject2}: "))
if classes2 < 0:
    print("value must be a positive number")
    exit()

duration2 = int(input(f"Enter duration of one class for {subject2}: "))
if duration2 <= 0:
    print("value must be a positive number")
    exit()

minutes1 = classes1 * duration1
minutes2 = classes2 * duration2
total_minutes = minutes1 + minutes2
total_hours = total_minutes / 60

available_hours = float(input("Enter available time for the week (in hours): "))
if available_hours < total_hours:
    print(f"available time cannot be less than total workload).")
    exit()

free_hours = available_hours - total_hours
minutes_4_weeks = total_minutes * 4
hours_4_weeks = total_hours * 4

print(f"Time for {subject1}: {minutes1} min")
print(f"Time for {subject2}: {minutes2} min")
print(f"Total workload: {total_minutes} min ({total_hours:.2f})")
print(f"Remaining free time: {free_hours:.2f} hrs")
print(f"4-week workload: {minutes_4_weeks} min ({hours_4_weeks:.2f})")
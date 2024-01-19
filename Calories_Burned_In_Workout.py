# Write a program using inputs age (years), weight (pounds), heart rate (beats per minute),
# and time (minutes), respectively. Output the average calories burned for a person.

age = int(input())
weight = int(input())
heartRate = int(input())
time = int(input())
calories = ((age * 0.2757) + (weight * 0.03295) + (heartRate * 1.0781) - 75.4991) * time / 8.368

print(f'Calories: {calories:.2f} calories')
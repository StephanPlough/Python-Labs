'''Write a program using inputs age (years), weight (pounds), heart rate (beats per minute),
 and time (minutes), respectively. Output the average calories burned for a person.'''

age = int(input("Enter age: "))
weight = int(input("Enter weight: "))
heartRate = int(input("Enter heart rate: "))
time = int(input("Enter time of workout in minutes: "))

calories_burned = ((age * 0.2757) + (weight * 0.03295) + (heartRate * 1.0781) - 75.4991) * time / 8.368
print(f'Calories: {calories_burned:.2f} calories')
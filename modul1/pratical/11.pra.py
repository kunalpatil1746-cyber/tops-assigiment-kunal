# Calculate grade based on percentage

percentage = float(input("Enter your percentage: "))

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Your Grade is:", grade)
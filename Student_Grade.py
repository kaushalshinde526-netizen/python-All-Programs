# Student Grade Analyzer

total_marks = 0
subjects = 5

for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    total_marks += marks

# Calculate percentage
percentage = total_marks / subjects

# Assign grade
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# Pass/Fail status
status = "Pass" if percentage >= 40 else "Fail"

# Output
print("\n------ Result ------")
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Status:", status)
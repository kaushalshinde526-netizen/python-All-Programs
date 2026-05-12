# Expense Splitter

total_amount = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))

# Calculate tip
tip_amount = (total_amount * tip_percent) / 100

# Final total
final_amount = total_amount + tip_amount

# Per person share
per_person = final_amount / num_people

print("\n------ Bill Summary ------")
print("Original Amount:", total_amount)
print("Tip Amount:", tip_amount)
print("Final Amount:", final_amount)
print("Each Person Pays:", round(per_person, 2))
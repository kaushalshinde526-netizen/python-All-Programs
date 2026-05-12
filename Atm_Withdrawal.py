# ATM Withdrawal Simulation

balance = float(input("Enter your account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

# Check conditions
if withdraw <= 0:
    print("Invalid amount!")
elif withdraw % 100 != 0:
    print("Amount should be in multiples of 100!")
elif withdraw > balance:
    print("Insufficient balance!")
else:
    balance -= withdraw
    print("\nTransaction Successful ✅")
    print("Withdrawn Amount:", withdraw)
    print("Remaining Balance:", balance)
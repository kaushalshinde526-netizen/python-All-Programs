balance = 5000
withdraw = int(input("Enter amount: "))

if withdraw % 100 != 0:
    print("Invalid Amount")
elif balance - withdraw < 1000:
    print("Insufficient Balance")
else:
    print("Transaction Successful")

    print("By Kaushal")
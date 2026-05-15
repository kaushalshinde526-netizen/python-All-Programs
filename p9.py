# WAPP TO PRINT 1 TO N
from time import sleep
n = int(input("Enter a number: "))

if n > 0:
    for i in range(1, n + 1, 1):
        print(i)
        sleep(1)	
else:
    print("invalid input")
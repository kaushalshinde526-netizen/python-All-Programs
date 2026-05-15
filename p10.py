#WAPP to print from 1 to n 
from time import sleep
n = int(input("enter n"))
if n>0:
	for i in range(1,n+1,1):
		print(i)
	sleep(1)
else:
	print("invalid input")
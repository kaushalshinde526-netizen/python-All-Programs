#Wapp to print n integer factorial 
n=int(input("Enter a factorial for : "))
if n>=0:
    i=1
    fact=1
    while i<=n:
      fact = fact*i
      i=i+1
    
    print("factorial : ",fact)
else :
   print("invalid input")
     
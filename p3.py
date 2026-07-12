class InterviewPrograms:

    def palindrome(self):
        s = input("Enter String: ")
        if s == s[::-1]:
            print("Palindrome")
        else:
            print("Not Palindrome")

    def anagram(self):
        s1 = input("Enter First String: ")
        s2 = input("Enter Second String: ")

        if sorted(s1) == sorted(s2):
            print("Anagram")
        else:
            print("Not Anagram")

    def prime(self):
        n = int(input("Enter Number: "))

        if n < 2:
            print("Not Prime")
            return

        for i in range(2, n):
            if n % i == 0:
                print("Not Prime")
                return

        print("Prime Number")

    def factorial(self):
        n = int(input("Enter Number: "))
        fact = 1

        for i in range(1, n + 1):
            fact *= i

        print("Factorial =", fact)

    def fibonacci(self):
        n = int(input("Enter Number of Terms: "))

        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b

        print()

    def reverse_string(self):
        s = input("Enter String: ")
        print("Reverse =", s[::-1])

    def reverse_number(self):
        n = int(input("Enter Number: "))
        rev = 0

        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10

        print("Reverse =", rev)

    def even_odd(self):
        n = int(input("Enter Number: "))

        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")

    def largest(self):
        nums = list(map(int, input("Enter numbers: ").split()))
        print("Largest =", max(nums))

    def armstrong(self):
        n = int(input("Enter Number: "))
        temp = n
        total = 0
        digits = len(str(n))

        while temp > 0:
            digit = temp % 10
            total += digit ** digits
            temp //= 10

        if total == n:
            print("Armstrong Number")
        else:
            print("Not Armstrong")


obj = InterviewPrograms()

while True:

    print("\n------ MENU ------")
    print("1. Palindrome")
    print("2. Anagram")
    print("3. Prime")
    print("4. Factorial")
    print("5. Fibonacci")
    print("6. Reverse String")
    print("7. Reverse Number")
    print("8. Even Odd")
    print("9. Largest")
    print("10. Armstrong")
    print("0. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        obj.palindrome()

    elif choice == 2:
        obj.anagram()

    elif choice == 3:
        obj.prime()

    elif choice == 4:
        obj.factorial()

    elif choice == 5:
        obj.fibonacci()

    elif choice == 6:
        obj.reverse_string()

    elif choice == 7:
        obj.reverse_number()

    elif choice == 8:
        obj.even_odd()

    elif choice == 9:
        obj.largest()

    elif choice == 10:
        obj.armstrong()

    elif choice == 0:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
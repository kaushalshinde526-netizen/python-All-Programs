# class Calculator:
#     def __init__(self):
#         self.a=int(input("Enter Positive Number a "))
#         self.b=int(input("Enter positive number  b "))
#     def add(self):
#         result = self.a + self.b
#         print("Addition =", result)
#     def mult(self):
#         result=self.a*self.b
# cal=Calculator()
# cal.add()
# cal.mult
class Calculator:

    def get_input(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))

    def add(self):
        self.get_input()
        print("Addition =", self.a + self.b)
        
        print("__________________________MULTIPLICATION____________________________________________")


    def mult(self):
        self.get_input()
        print("Multiplication =", self.a * self.b)
    
        print("_________________________________Division__________________________________________________")
    
    def Div(self):
        try:
            self.get_input()

            if self.a <= 0 or self.b <= 0:
                raise ValueError

            print("Division =", self.a / self.b)

        except ValueError:
            print("Number should be grater than zero .")


cal = Calculator()
cal.add()
cal.mult()
cal.Div()
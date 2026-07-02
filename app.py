# import math
# import json
# from datetime import datetime

# #Base class
# class Calculator:
#     def __init__(self):
#         self.history=[]
#     def add(self a,b):
#         return a+b
#     def substract(self,a,b):
#         return a-b
#     def multiply(self,a,b):
#         return a*b
#     def divide(self,a,b):
#         if b==0:
#             raise ValueError("Cannot divide By Zero")
#         return a/b
#     def save_to_history(self,operation,a,b, result):
#         entry={"timestam": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"opertion":operation,"inputs":f"{a} and {b}", "result":result}
#         self.history.append(entry)
#     def show_history(self):
#         if not self.history:
#             print("No calculations yet!")
#             return
#         print("\n==Calculations History ===")
#         for i, enter in enumerate(self.history[-10:],1):
#             print(f"{i}.[{entry['timestamp']}]{entry['operation']}:{entry['inputs']}={entry['result']}")
# #Inherited class (Scientific calculation)
# class ScientificCaculator(Calculator)
#     def power(self,a,b):
#         return a**b
#     def square_root(self,a):
#         if a<0:
#             raise ValueError("Cannot take square root of negative num")
#             return math.sqrt(a)

import math
import json
from datetime import datetime

# Base Class
class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    def save_to_history(self, operation, a, b, result):
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operation": operation,
            "inputs": f"{a} and {b}",
            "result": result
        }
        self.history.append(entry)
    
    def show_history(self):
        if not self.history:
            print("No calculations yet!")
            return
        print("\n=== Calculation History ===")
        for i, entry in enumerate(self.history[-10:], 1):  # Last 10
            print(f"{i}. [{entry['timestamp']}] {entry['operation']}: {entry['inputs']} = {entry['result']}")


# Inherited Class (Scientific Calculator)
class ScientificCalculator(Calculator):
    def power(self, a, b):
        return a ** b
    
    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number!")
        return math.sqrt(a)
    
    def logarithm(self, a):
        if a <= 0:
            raise ValueError("Logarithm only defined for positive numbers!")
        return math.log10(a)


# Main Application Class (Handles Menu)
class CalculatorApp:
    def __init__(self):
        self.calc = ScientificCalculator()
    
    def clear_screen(self):
        print("\n" * 50)  # Simple clear
    
    def display_menu(self):
        print("="*40)
        print("   🧮  OOP CALCULATOR  🧮")
        print("="*40)
        print("1.  Addition")
        print("2.  Subtraction")
        print("3.  Multiplication")
        print("4.  Division")
        print("5.  Power (a^b)")
        print("6.  Square Root")
        print("7.  Logarithm (base 10)")
        print("8.  Show History")
        print("9.  Clear History")
        print("0.  Exit")
        print("="*40)
    
    def get_number(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("❌ Error: Please enter a valid number!")
    
    def perform_operation(self, choice):
        try:
            if choice in ['1', '2', '3', '4', '5']:
                a = self.get_number("Enter first number: ")
                b = self.get_number("Enter second number: ")
            else:
                a = self.get_number("Enter number: ")
                b = None

            if choice == '1':
                result = self.calc.add(a, b)
                op_name = "Addition"
            elif choice == '2':
                result = self.calc.subtract(a, b)
                op_name = "Subtraction"
            elif choice == '3':
                result = self.calc.multiply(a, b)
                op_name = "Multiplication"
            elif choice == '4':
                result = self.calc.divide(a, b)
                op_name = "Division"
            elif choice == '5':
                result = self.calc.power(a, b)
                op_name = "Power"
            elif choice == '6':
                result = self.calc.square_root(a)
                op_name = "Square Root"
            elif choice == '7':
                result = self.calc.logarithm(a)
                op_name = "Logarithm"
            else:
                return

            # Format result
            if isinstance(result, float):
                result = round(result, 6)
            
            print(f"\n✅ Result: {result}")
            self.calc.save_to_history(op_name, a, b if b is not None else "", result)

        except ValueError as ve:
            print(f"❌ Error: {ve}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def run(self):
        while True:
            self.clear_screen()
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (0-9): ").strip()
                
                if choice == '0':
                    print("Thank you for using OOP Calculator! 👋")
                    break
                elif choice == '8':
                    self.calc.show_history()
                elif choice == '9':
                    self.calc.history.clear()
                    print("History cleared!")
                elif choice in ['1','2','3','4','5','6','7']:
                    self.perform_operation(choice)
                else:
                    print("❌ Invalid choice! Please select 0-9.")
                
                input("\nPress Enter to continue...")
                
            except Exception as e:
                print(f"Error: {e}")
                input("Press Enter to continue...")


# Run the application
if __name__ == "__main__":
    app = CalculatorApp()
    app.run()

    
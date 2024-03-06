#create class Calculator
class Calculator():
    def add(self, x, y):
        return x + y
    def minus(self, x,y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        return x / y
    
print("Choose operation:\n 1:Addition\n 2:Subtraction\n 3:Multiplication\n")

while True:
    operation = float(input("Enter 1/2/3/4:"))

    if operation == 1 | 2 | 3 | 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    else:
        print("Input is invalid.")

        if operation == 1:
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operation == 2:
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == 3:
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == 4:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    



        
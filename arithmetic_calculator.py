#create class Calculator
class Calculator():
    def add(self, x, y):
        return x + y
    def minus(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        return x / y
    
print("Choose operation:\n 1:Addition\n 2:Subtraction\n 3:Multiplication\n 4:Division")

#Prompt user to make a choice 1-4
operation = (input("Enter 1/2/3/4: "))

while operation in (str(1),str(2),str(3),str(4)):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
#else:
    #print("Invalid input")
    
#call the Calculator() class
    calc = Calculator()

    if operation == str(1):
        print(f"{num1} + {num2} = {calc.add(num1, num2)}")
    elif operation == str(2):
        print(f"{num1} - {num2} = {calc.minus(num1, num2)}")
    elif operation == str(3):
        print(f"{num1} * {num2} = {calc.multiply(num1, num2)}")
    elif operation == str(4):
        print(f"{num1} / {num2} = {calc.divide(num1, num2)}")
    else:
        print("Input is not a number")
else:
    print("Wrong choice, choose between 1,2,3,4")
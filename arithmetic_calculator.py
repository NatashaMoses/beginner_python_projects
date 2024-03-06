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
    
print("Choose operation:\n 1:Addition\n 2:Subtraction\n 3:Multiplication\n 4:Division")


    #Prompt user to make a choice 1-4
operation = float(input("Enter 1/2/3/4: "))

while operation in (1,2,3,4):
        try:
            num1 = (input("Enter first number: "))
            num2 = (input("Enter second number: "))
        except:
            print("Invalid input")
            #continue

        #call the Calculator() class
        calc = Calculator()

        if operation == '1':
            print(f"{num1} + {num2} = {calc.add(num1, num2)}")
        elif operation == '2':
            print(f"{num1} - {num2} = {calc.minus(num1, num2)}")
        elif operation == '3':
            print(f"{num1} * {num2} = {calc.multiply(num1, num2)}")
        elif operation == '4':
            print(f"{num1} / {num2} = {calc.divide(num1, num2)}")
        else:
            print("Input is not a float")            

        break   



        
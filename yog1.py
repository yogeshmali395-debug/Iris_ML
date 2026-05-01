# user se input lena
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# operation lena
operation = input("Enter operation (+, -, *, /): ")

# calculation logic
if operation == "+":
    print("Result of Addition:", num1 + num2)

elif operation == "-":
    print("Result of Substraction:", num1 - num2)

elif operation == "*":
    print("Result of Multiplication:", num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("Result of Devide:", num1 / num2)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operation")

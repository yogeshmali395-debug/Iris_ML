# user se input lena
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# operation lena
op = input("Enter operation (+, -, *, /): ")

# calculation logic
if op == "+":
    print("Result of Addition:", num1 + num2)

elif op == "-":
    print("Result of Substraction:", num1 - num2)

elif op == "*":
    print("Result of Multiplication:", num1 * num2)

elif op == "/":
    if num2 != 0:
        print("Result of Devide:", num1 / num2)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operation")

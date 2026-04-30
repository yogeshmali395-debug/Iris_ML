# user se input lena
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# operation lena
op = input("Enter operation (+, -, *, /): ")

# calculation logic
if op == "+":
    print("Result:", num1 + num2)

elif op == "-":
    print("Result:", num1 - num2)

elif op == "*":
    print("Result:", num1 * num2)

elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operation")

print("Calculator")
a = float(input("Enter the first number : "))
b = str(input("Enter the sing : "))
c = float(input("Enter the second number : "))

if b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "*":
    print(a * c)
elif b == "/" and c == 0:
    print("division by zero")
elif  b == "/":
    print(a / c)
else:
    print("Please enter a valid input")
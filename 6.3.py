user_number = int(input("Enter a number: "))

while user_number > 9:
    product = 1

    for digit in str(user_number):
        product *= int(digit)

    user_number = product

print(user_number)
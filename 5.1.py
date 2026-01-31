import keyword
import string

variable = input("Enter a variable: ")

if not variable:
    print(False)
else:
    if variable[0].isdigit():
        print(False)


    elif any(char.isupper() for char in variable):
        print(False)

    elif ' ' in variable:
        print(False)


    elif any(char in string.punctuation.replace('_', '') for char in variable):
        print(False)

    elif variable in keyword.kwlist:
        print(False)

    else:
        print(True)
    print("Thanks for valid input")

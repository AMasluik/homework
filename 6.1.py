import string

letters = input("Enter two letters: ")

a, b = letters.split('-')

first_index = string.ascii_letters.index(a)
second_index = string.ascii_letters.index(b)

print(string.ascii_letters[first_index:second_index + 1])





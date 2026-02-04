import string

letters_input = input("Enter two letters: ")

first_letter, second_letter = letters_input.split('-')

first_position = string.ascii_letters.index(first_letter)
second_position = string.ascii_letters.index(second_letter)

letters_range = string.ascii_letters[first_position:second_position + 1]
print(letters_range)





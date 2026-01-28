numbers = []

if not numbers:
    numbers = [0]

sum_even_index = 0
for i in range(0, len(numbers), 2):
    sum_even_index += numbers[i]

result = sum_even_index * numbers[-1]
print(result)  

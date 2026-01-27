numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

index = 0

for i, num in enumerate(numbers):
    if num != 0:
        numbers[index] = num
        index += 1

for i in range(index, len(numbers)):
    numbers[i] = 0

print(numbers) #хочу через f строку можна?

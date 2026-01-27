import random

length = random.randint(3, 10)
numbers = [random.randint(1, 9) for _ in range(length)]

result = numbers[:3:2] + numbers[-2:-1]

print("List:", numbers)
print("Result:", result)


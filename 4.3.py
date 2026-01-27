import random

numbers = [random.randint(1, 9) for _ in range(random.randint(3, 9))]
result = numbers[:3:2] + numbers[-2:-1]

print(f"List: {numbers}")
print(f"Result: {result}")

# без рандома
numbers = [1, 2, 3, 4, 5, 6, 7, 9]
result = numbers[:3:2] + numbers[-2:-1]
print(f"List: {numbers}")
print(f"Result: {result}")

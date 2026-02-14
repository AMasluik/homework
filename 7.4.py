def common_elements():
    return set(range(0, 100, 3)) & set(range(0, 100, 5))

result = common_elements()
#print(f"Result: {result}") если нужно то вот 
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}#но я думаю что у нас есть проверка и принт не особо имеет смысл 



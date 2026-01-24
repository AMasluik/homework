lst = [12, 3, 4, 10]
if len(lst) > 1:
    lst = lst[-1:] + lst[:-1]
print(lst)
#не знаю какой из вариантов мне больше нравиться
lst = []
lst = lst[-1:] + lst[:-1]
print(lst)

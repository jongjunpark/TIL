number = list(range(1,11))
result = list(filter(lambda x: x % 2 == 0, number))
result2 = list(map(lambda x: x * x, result))
print(result2)
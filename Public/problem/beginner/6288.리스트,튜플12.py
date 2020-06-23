list1 = list(range(1,21))

result = [i * i for i in list1 if (i % 3 != 0) or (i % 5 != 0)]

print(result)

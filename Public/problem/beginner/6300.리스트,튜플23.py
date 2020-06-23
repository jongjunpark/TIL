list1 = [12, 24, 35, 70, 88, 120, 155]
result = [val for idx, val in enumerate(list1) if idx % 2 != 0]

print(result)
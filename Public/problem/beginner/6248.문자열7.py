input1 = str(input())
list1 = list(input1)

result = [val for idx, val in enumerate(list1) if idx % 2 == 0]
print(''.join(result))
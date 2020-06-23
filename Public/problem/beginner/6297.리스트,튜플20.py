input1 = list(map(int, input().split(', ')))

result = [i for i in input1 if i % 2 != 0]

final = ', '.join(map(str,result))
print(final)

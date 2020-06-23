input1 = int(input())
result = []

for i in range(1,input1 + 1):
    if input1 % i == 0:
        result.append(i)

print(result)
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = []
for i in list_a[1:9]:
    qwe = []
    for j in list_a:
        qwe.append(i * j)
        result2 = [num for num in qwe if (num % 3 != 0) and (num % 7 != 0)]
    result.append(result2)
print(result)

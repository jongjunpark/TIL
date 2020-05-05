a = input()
result = []
tmp = ''
for i in range(len(a)):
    if a[i] == ' ':
        result.append(tmp)
        tmp = ''
    elif i == len(a)-1:
        tmp += a[i]
        result.append(tmp)
    else:
        tmp += a[i]
for j in range(1,len(result)+1):
    print(result[-j], end=' ')

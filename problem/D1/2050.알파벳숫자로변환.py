alpha = input()
num = list(range(1,27))
for i in alpha:
    a = ord(i)
    print(num[a-65],end=' ')
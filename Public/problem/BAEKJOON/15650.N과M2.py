def numbering(a,b):
    global result
    if b == M:
        k = result[:]
        result.sort()
        if result not in x:
            x.append(k)
        result = k[:]
        return
    for i in range(1,a+1):
        if i not in check:
            result[b] = i
            check[b] = i
            numbering(a,b+1)
        check[b] = 0
        result[b] = 0

N, M = map(int,input().split())
result = [0] * M
check = [0] * M
x = []
numbering(N,0)

for i in x:
    print(' '.join(map(str,i)))
def numbering(a,b):
    if b == M:
        print(' '.join(map(str,result)))
        return
    for i in range(1,a+1):
        if b == 0:
            result[b] = i
            numbering(a, b + 1)
        elif result[b-1] <= i:
            result[b] = i
            numbering(a,b+1)

N, M = map(int,input().split())
result = [0] * M
numbering(N,0)
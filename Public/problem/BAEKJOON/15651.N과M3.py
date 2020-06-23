def numbering(a,b):
    if b == M:
        print(' '.join(map(str,result)))
        return
    for i in range(1,a+1):
        result[b] = i
        numbering(a,b+1)

N, M = map(int,input().split())
result = [0] * M
numbering(N,0)
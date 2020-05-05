def nodesum(x):
    if x == 0:
        return
    if x*2+1 <= N:
        arr[x] = arr[x*2] + arr[x*2+1]
    elif x*2 <= N:
        arr[x] = arr[x*2]
    nodesum(x-1)

for t in range(1, int(input())+1):
    N, M, L = map(int,input().split())
    arr = [0]*(N+1)
    for _ in range(M):
        a, b = map(int,input().split())
        arr[a] = b
    nodesum(N-M)
    print('#{} {}'.format(t,arr[L]))
def subtree(node):
    global cnt
    if arr[0][node]:
        cnt += 1
        subtree(arr[0][node])
    if arr[1][node]:
        cnt += 1
        subtree(arr[1][node])
    else:
        return

for t in range(1, int(input())+1):
    E, N = map(int,input().split())
    num = list(map(int,input().split()))
    arr = [[0] * (max(num)+1) for _ in range(2)]
    for i in range(E):
        if arr[0][num[i*2]] == 0:
            arr[0][num[i*2]] = num[i*2+1]
        else:
            arr[1][num[i*2]] = num[i*2+1]
    cnt = 1
    subtree(N)
    print('#{} {}'.format(t,cnt))
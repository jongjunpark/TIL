def my_func(r):
    global total, min_total
    if r == N:
        if total < min_total:
            min_total = total
        return
    for j in range(N):
        if arr[r][j] > 0:
            continue
        total += num[r][j]
        if total > min_total:
            total -= num[r][j]
            continue
        marking(r,j)
        my_func(r+1)
        total -= num[r][j]
        un_marking(r,j)

def marking(r,c):
    for i in range(N):
        arr[i][c] += 1
        arr[r][i] += 1

def un_marking(r,c):
    for i in range(N):
        arr[i][c] -= 1
        arr[r][i] -= 1

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = [list(map(int,input().split())) for _ in range(N)]
    arr = [[0]*N for _ in range(N)]
    total = 0
    min_total = 100000
    my_func(0)
    print('#{} {}'.format(t,min_total))
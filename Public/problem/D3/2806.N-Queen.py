def n_queen(r):
    global count
    if r == N:
        count += 1
        return
    for i in range(N):
        if arr[r][i] > 0:
            continue
        marking(r,i)
        n_queen(r+1)
        un_marking(r,i)


def marking(r,c):
    for i in range(N):
        arr[r][i] += 1
        arr[i][c] += 1

    for i in range(N):
        if r+i < N and c+i < N:
            arr[r+i][c+i] += 1

    for i in range(N):
        if r+i < N and c-i >= 0:
            arr[r+i][c-i] += 1

def un_marking(r,c):
    for i in range(N):
        arr[r][i] -= 1
        arr[i][c] -= 1

    for i in range(N):
        if r+i < N and c+i < N:
            arr[r+i][c+i] -= 1

    for i in range(N):
        if r+i < N and c-i >= 0:
            arr[r+i][c-i] -= 1

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    count = 0
    n_queen(0)
    print('#{} {}'.format(t,count))
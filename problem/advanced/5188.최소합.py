def arr_sum(a,b,t):
    global min_sum
    if a == N-1 and b == N-1:
        if t <= min_sum:
            min_sum = t
        return
    else:
        if a+1 <= N-1:
            arr_sum(a+1,b,t+arr[a+1][b])
        if b+1 <= N-1:
            arr_sum(a,b+1,t+arr[a][b+1])

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_sum = 1000000
    arr_sum(0,0,arr[0][0])
    print('#{} {}'.format(tc, min_sum))
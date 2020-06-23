def arr_sum(a,b,t,cnt):
    global min_sum
    if cnt == N-1:
        if t+arr[b][0] <= min_sum:
            min_sum = t+arr[b][0]
        return
    else:
        for k in range(N):
            if k == b:
                continue
            if visited[k]:
                continue
            else:
                visited[b] = 1
                arr_sum(b,k,t+arr[b][k],cnt+1)
                visited[b] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_sum = 1000000
    for i in range(1,N):
        visited = [0]*N
        visited[0] = 1
        arr_sum(0,i,arr[0][i],1)
    print('#{} {}'.format(tc,min_sum))

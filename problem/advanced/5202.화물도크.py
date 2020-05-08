def day_work(a,s):
    global max_work
    for i in range(N):
        if time[a][1] <= time[i][0]:
            day_work(i,s+1)
    if s >= max_work:
        max_work = s
    return

for tc in range(1, int(input())+1):
    N = int(input())
    time = [list(map(int,input().split())) for _ in range(N)]
    max_work = 0
    value = 1000
    start = 0
    for k in range(N):
        if time[k][1] <= value:
            value = time[k][1]
            start = k
    day_work(start,1)
    print('#{} {}'.format(tc,max_work))
def search(i,j,cnt=1):
    global max_cnt, min_room
    delta = [(1,0),(0,1),(-1,0),(0,-1)]
    for k in range(4):
        dx,dy = delta[k]
        x = i + dx
        y = j + dy
        if 0 <= x < N and 0 <= y < N and arr[x][y] == (arr[i][j]+1):
            search(x,y,cnt+1)
    else:
        if cnt > 1:
            if cnt > max_cnt:
                max_cnt = cnt
                min_room = arr[i][j] - cnt + 1
            elif cnt == max_cnt:
                max_cnt = cnt
                if arr[i][j] - cnt + 1 < min_room:
                    min_room = arr[i][j] - cnt + 1
            return
        else:
            if j == N-1:
                return
            elif j < N-1:
                return search(i,j+1,cnt)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_cnt = 0
    min_room = N * N
    for i in range(N):
        search(i,0)
    print('#{} {} {}'.format(t,min_room, max_cnt))
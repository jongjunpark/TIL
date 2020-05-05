def news(i,j,s):
    global tmp
    delta = [(0,1),(1,0),(-1,0),(0,-1)]
    tmp += arr[i][j]
    if s == 7:
        result.add(tmp)
        return
    for k in range(4):
        dx,dy = delta[k]
        x,y = i+dx, j+dy
        if 0<= x < 4 and 0<= y < 4:
            news(x,y,s+1)
            tmp = tmp[:-1]

T = int(input())
for t in range(1, T + 1):
    N = 4
    arr = [list(map(str, input().split())) for _ in range(4)]
    result = {0}
    for i in range(N):
        for j in range(N):
            tmp = ''
            news(i, j, 1)
    print('#{} {}'.format(t,len(result)-1))
def BFS():
    while q:
        i,j = q.pop(0)
        for k in range(4):
            dx,dy = delta[k]
            x = i + dx
            y = j + dy
            if 0<=x<M and 0<=y<N and tomato[x][y]==0 and visited[x][y] == 0:
                q.append((x,y))
                visited[x][y] = visited[i][j] + 1
    return

N, M = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
delta = [(1,0), (0,1), (-1,0), (0,-1)]
q = []
for i in range(M):
    for j in range(N):
        if tomato[i][j] == -1:
            visited[i][j] = -1
        elif tomato[i][j] == 1:
            q.append((i,j))
            visited[i][j] = 1
BFS()
max_num = -1
flag = False
for i in range(M):
    if flag:
        break
    for j in range(N):
        if visited[i][j] == 0:
            flag = True
            break
        else:
            if visited[i][j] - 1 > max_num:
                max_num = visited[i][j] - 1
print(max_num)
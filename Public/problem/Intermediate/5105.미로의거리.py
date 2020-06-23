def BFS(maze):
    delta = [(0,1), (1,0), (0,-1), (-1,0)] #우 하, 좌, 상
    while queue:
        p,q = queue.pop(0)
        for k in range(4):
            dx,dy = delta[k]
            x = p + dx
            y = q + dy
            if 0<=x<N and 0<=y<N and maze[x][y] == 0 and visited[x][y] == 0 and visited[x][y] == 0:
                visited[x][y] = visited[p][q] + 1
                queue.append((x,y))
            if 0<=x<N and 0<=y<N and maze[x][y] == 3:
                return print('#{} {}'.format(tc, visited[p][q]))
    return print('#{} 0'.format(tc))


for tc in range(1,int(input())+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    queue = []
    visited = [[0] * N for _ in range(N)]
    a = False
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                queue.append((i,j))
                a = True
                break
        if a == True:
            break
    BFS(maze)
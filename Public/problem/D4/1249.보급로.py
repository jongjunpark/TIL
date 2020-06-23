T = int(input())
for tc in range(1, T+1):
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)]
    visited = [[float('inf')]*N for _ in range(N)]
    queue = [(0,0)]
    visited[0][0] = 0
    while queue:
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i,j = queue.pop(0)
        for k in range(4):
            dx, dy = delta[k]
            x = i + dx
            y = j + dy
            if 0 <= x < N and 0 <= y < N:
                if visited[x][y] > visited[i][j] + road[x][y]:
                    visited[x][y] = visited[i][j] + road[x][y]
                    queue.append((x,y))
    print('#{} {}'.format(tc,visited[-1][-1]))

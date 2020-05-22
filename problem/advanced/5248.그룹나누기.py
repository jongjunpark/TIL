for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    mat = [[0]*(N+1) for _ in range(N+1)]
    path = list(map(int,input().split()))
    for i in range(0,M*2,2):
        mat[path[i]][path[i+1]] = 1
        mat[path[i+1]][path[i]] = 1
    visited = [0]*(N+1)
    cnt = -1
    for i in range(N+1):
        if visited[i] == 0:
            cnt += 1
            visited[i] = 1
        for j in range(N+1):
            if mat[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                queue = []
                queue.append(j)
                while queue:
                    x = queue[0]
                    for y in range(N+1):
                        if mat[x][y] == 1 and visited[y] == 0:
                            visited[y] = 1
                            queue.append(y)
                    else:
                        queue.pop(0)
    print('#{} {}'.format(tc,cnt))
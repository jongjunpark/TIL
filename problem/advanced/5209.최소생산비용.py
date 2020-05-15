def min_manufacture(i, j, s):
    global min_rate
    if s >= min_rate:
        return
    if i == N-1:
        min_rate = s
        return
    else:
        for k in range(N):
            visited[k][j] = 1
        for l in range(N):
            if visited[i+1][l] == 0:
                min_manufacture(i+1, l, s+rate[i+1][l])
        for k in range(N):
            visited[k][j] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    rate = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    min_rate = 1000000
    for j in range(N):
        min_manufacture(0, j, rate[0][j])
    print('#{} {}'.format(tc,min_rate))
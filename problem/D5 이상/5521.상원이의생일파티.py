T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    rel = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int, input().split())
        rel[a][b] = 1
        rel[b][a] = 1
    friend = set()
    for i in range(N+1):
        if rel[1][i]:
            friend.add(i)
            for j in range(N+1):
                if rel[i][j]:
                    friend.add(j)
    if len(friend):
        print('#{} {}'.format(tc,len(friend)-1))
    else:
        print('#{} 0'.format(tc))
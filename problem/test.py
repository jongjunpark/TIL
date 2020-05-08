import sys

sys.stdin = open('input.txt', 'r')

def delicious(data, s, t):
    global max_score
    for i in range(N):
        if visited[i] == 1:
            continue
        if t + data[i][1] > L:
            continue
        else:
            visited[i] = 1
            delicious(data, s+data[i][0], t+data[i][1])
            visited[i] = 0
    if s >= max_score:
        max_score = s
    return


for tc in range(1, int(input())+1):
    N, L = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    max_score = 0
    visited = [0]*N

    for i in range(N):
        visited[i] = 1
        delicious(data, data[i][0], data[i][1])
        visited[i] = 0
    print('#{} {}'.format(tc,max_score))



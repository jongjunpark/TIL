import sys

sys.stdin = open("input.txt", "r")

def queen(idx):
    global cnt
    if idx == N:
        cnt += 1
        return
    for i in range(N):
        if visited[idx][i] == 0:
            marking(idx,i)
            queen(idx+1)
            un_marking(idx,i)

def marking(i,j):
    for k in range(N):
        visited[i][k] = 1
        visited[k][j] = 1
        if 0<=i+k<N and 0<=j+k<N:
            visited[i+k][j+k] = 1
        if 0<=i-k<N and 0<=j-k<N:
            visited[i - k][j - k] = 1

def un_marking(i,j):
    for k in range(N):
        visited[i][k] = 0
        visited[k][j] = 0
        if 0<=i+k<N and 0<=j+k<N:
            visited[i+k][j+k] = 0
        if 0<=i-k<N and 0<=j-k<N:
            visited[i - k][j - k] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for i in range(N):
        visited = [[0] * N for _ in range(N)]
        marking(0,i)
        queen(1)
    print('#{} {}'.format(tc,cnt))











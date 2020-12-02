import sys

sys.stdin = open("input.txt", "r")


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[0]*(N) for _ in range(N)]
    start_point = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 1:
                start_point.append((i,j))

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    times = [list(map(int, input().split())) for _ in range(M)]
    arr = [[0]*N for _ in range(N)]
    arr[N//2][N//2],arr[N//2-1][N//2-1] = 2,2
    arr[N//2-1][N//2], arr[N//2][N//2-1] = 1,1
    for i in range(M):



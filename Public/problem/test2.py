import sys,heapq

sys.stdin = open('input.txt', 'r')

def road_sum(i,j,s):
    global min_sum
    if s > min_sum:
        return
    if i == N-1 and j == N-1:
        min_sum = s
        return
    if i+1 < N:
        road_sum(i+1,j,s+road[i+1][j])
    if j+1 < N:
        road_sum(i,j+1,s+road[i][j+1])
    if i-1 >= 0:
        road_sum(i-1,j,s+road[i-1][j])
    if j-1 >= 0:
        road_sum(i,j-1,s+road[i][j-1])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)]
    min_sum = 0
    for i in range(N):
        min_sum += road[0][i]
        min_sum += road[i][-1]
    road_sum(0,0,0)
    print(min_sum)

# 공간의 크기 N
# 이동할 계획서 내용

import sys
sys.stdin=open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    root = input().split()

    i,j = 0,0
    delta = { 'L': (0,-1), 'R': (0,1), 'U': (-1,0), 'D': (1,0) }

    for k in root:
        dx, dy = delta[k]
        x = i + dx
        y = j + dy

        if 0 <= x < N and 0 <= y < N:
            i,j = x,y

    print(i+1, j+1)

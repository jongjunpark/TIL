# 8x8 좌표
import sys
sys.stdin=open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    point = input()
    cnt = 0

    delta = ((1,2), (-1,2), (1,-2), (-1,-2), (2,1), (-2,1), (2,-1), (-2,-1))

    i_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

    i = i_dict[point[0]]
    j = int(point[1]) - 1

    for dx,dy in delta:
        x = i + dx
        y = j + dy

        if 0 <= x < 8 and 0 <= y < 8:
            cnt += 1
        
    print(cnt)
    
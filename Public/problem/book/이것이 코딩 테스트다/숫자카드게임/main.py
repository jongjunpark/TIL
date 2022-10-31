# 행의 갯수 N, 열의 갯수 M
# 1 <= N,M <= 100
import sys
sys.stdin=open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    result = 0
    for i in range(N):
        numbers = list(map(int, input().split()))
        min_number = min(numbers)
        
        if min_number > result:
            result = min_number
    print(result)
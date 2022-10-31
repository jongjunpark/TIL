# 숫자 N, 나누려는 숫자 K
# 2 <= N,K <= 100,000
import sys
sys.stdin=open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    
    cnt = 0

    while N != 1:
        cnt += 1
        if N % K == 0:
            N //= K
        else:
            N -= 1
     
    print(cnt)
        
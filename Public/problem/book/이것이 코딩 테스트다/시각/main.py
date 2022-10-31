# 정수 N
# 0 <= N <= 23
import sys
sys.stdin=open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    result = 0
    for i in range(N+1):
      for j in range(60):
        for k in range(60):
          if '3' in str(i) or '3' in str(j) or '3' in str(k):
            result += 1
    
    print(result)
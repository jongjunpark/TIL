import sys

sys.stdin = open('input.txt', 'r')

def find(start, idx, cnt):
    global value, result
    if charge[idx] - start > K:
        return
    if cnt > value:
        return
    if start + K >= N:
        if value > cnt:
            value = cnt
            result = cnt
        return
    else:
        for j in range(1, M-abs(idx)+1):
            find(charge[idx], -j, cnt+1)
    

for tc in range(1,int(input())+1):
    temp = list(map(int, input().split()))
    K = temp[0]; N = temp[1]; M = temp[2]
    charge = list(map(int, input().split()))
    result = float('inf')
    if charge[0] > K:
        print(f'#{tc} 0')
    else:
        for i in range(M):
            value = float('inf')
            find(0, i, 0)
        if result == float('inf'):
            result = 0
        print(f'#{tc} {result}')
    

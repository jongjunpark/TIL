T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))
    check = [0]*N
    for i in range(M):
        for j in range(N):
            if Bi[i] >= Ai[j]:
                check[j] += 1
                break
    print('#{} {}'.format(t,check.index(max(check))+1))
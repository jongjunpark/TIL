def truck(a,b,s):
    global result
    if b == M or a == N:
        return print('#{} {}'.format(tc, s))
    if w[a] <= t[b]:
        truck(a+1,b+1,s+w[a])
    else:
        truck(a+1,b,s)
    return

for tc in range(1, int(input())+1):
    N, M = map(int,input().split())
    W = list(map(int,input().split()))
    T = list(map(int, input().split()))
    w = sorted(W, reverse=True)
    t = sorted(T, reverse=True)
    truck(0,0,0)
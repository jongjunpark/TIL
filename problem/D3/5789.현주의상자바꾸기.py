T = int(input())
for t in range(1, T+1):
    N, Q = map(int,input().split())
    box = [0]*N
    for q in range(Q):
        L, R = map(int,input().split())
        i = 0
        while L-1+i < R:
            box[L-1+i] = q+1
            i += 1
    print('#{} {}'.format(t,' '.join(map(str,box))))
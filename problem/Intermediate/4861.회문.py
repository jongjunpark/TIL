T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    data = []
    for i in range(N):
        tmp = input()
        tmp = list(tmp)
        data.append(tmp)
    a = list('a' * M)
    b = list('a' * M)
    for i in range(N):
        if type(a) == str:
            break
        for j in range(N - M + 1):
            for k in range(M):
                b[k] = data[i][k + j]
                a[-(k + 1)] = data[i][k + j]
            if a == b:
                a = ''.join(a)
                print('#{} {}'.format(t, a))
                break
        if type(a) == str:
            break

    for i in range(N):
        if type(a) == str:
            break
        for j in range(N - M + 1):
            for k in range(M):
                b[k] = data[k+j][i]
                a[-(k + 1)] = data[k+j][i]
            if a == b:
                a = ''.join(a)
                print('#{} {}'.format(t, a))
                break
for t in range(1,11):
    M = int(input())
    data = []
    for i in range(8):
        tmp = input()
        tmp = list(tmp)
        data.append(tmp)
    a = list('a' * M)
    b = list('a' * M)
    c = []
    for i in range(8):
        for j in range(8 - M + 1):
            for k in range(M):
                b[k] = data[i][k + j]
                a[-(k + 1)] = data[i][k + j]
            if a == b:
                c.append(''.join(a))

    for i in range(8):
        for j in range(8 - M + 1):
            for k in range(M):
                b[k] = data[k+j][i]
                a[-(k + 1)] = data[k+j][i]
            if a == b:
                c.append(''.join(a))

    print('#{} {}'.format(t,len(c)))

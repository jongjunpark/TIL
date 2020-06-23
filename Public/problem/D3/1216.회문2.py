for t in range(1,11):
    n = int(input())
    data = []
    for i in range(100):
        tmp = input()
        tmp = list(tmp)
        data.append(tmp)
    max_len = 0
    for i in range(100):
        for l in range(100):
            a = list('a' * l)
            b = list('a' * l)
            for j in range(100-l + 1):
                for k in range(l):
                    b[k] = data[i][k + j]
                    a[-(k + 1)] = data[i][k + j]
                if a == b and len(a)>max_len:
                    max_len = len(a)

    for i in range(100):
        for l in range(100):
            a = list('a' * l)
            b = list('a' * l)
            for j in range(100 - l + 1):
                for k in range(l):
                    b[k] = data[k+j][i]
                    a[-(k + 1)] = data[k+j][i]
                if a == b and len(a)>max_len:
                    max_len = len(a)

    print('#{} {}'.format(t,max_len))
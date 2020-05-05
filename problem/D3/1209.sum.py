for x in range(10):
    s = int(input())
    n = []
    for i in range(100):
        ns = list(map(int,input().split()))
        n.append(ns)
    max_v = 0
    for i in range(100):
        t1 = 0
        t2 = 0
        t3 = 0
        for j in range(100):
            t1 += n[i][j]
            t2 += n[j][i]
            if i == j or i + j == 100:
                t3 += n[i][j]
        if t1 > t2 and t1 > t3 and t1 > max_v:
            max_v = t1
        elif t2 > t1 and t2 > t3 and t2 > max_v:
            max_v = t2
        elif t3 > t1 and t3 > t2 and t3 > max_v:
            max_v = t3
    print(f'#{s} {max_v}')
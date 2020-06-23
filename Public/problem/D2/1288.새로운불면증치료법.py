T = int(input())
for t in range(1,T+1):
    N = int(input())
    set1 = {10}
    a = 1
    while True:
        n = str(N*a)
        for i in n:
            set1.add(i)
        a += 1
        if len(set1) == 11:
            break
    print(f'#{t} {n}')
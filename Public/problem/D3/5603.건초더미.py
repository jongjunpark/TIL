T = int(input())
for t in range(1,T+1):
    N = int(input())
    result = 0
    num = []
    for i in range(N):
        tmp = int(input())
        result += tmp
        num.append(tmp)
    avg = result // N
    count = 0
    for i in num:
        if i > avg:
            count += (i - avg)
    print('#{} {}'.format(t,count))
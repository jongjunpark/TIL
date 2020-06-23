T = int(input())
day_31 = [1,3,5,7,8,10,12]
for t in range(1, T+1):
    m, d = map(int,input().split())
    day = 0
    for i in range(1,m):
        if i in day_31:
            day += 31
        elif i == 2:
            day += 29
        else:
            day += 30
    day += (d-1)
    k = (day+4) % 7
    print('#{} {}'.format(t,k))

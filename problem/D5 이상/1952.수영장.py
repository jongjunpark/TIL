def swim(j):
    global min_fee, total
    if plan.count(0) == 12:
        if total < min_fee:
            min_fee = total          # 0 0 2 9 1 5 0 0 0 0 0 0
        return
    if plan[j] != 0:
        for i in range(3):
            if i == 0:
                x = plan[j]
                total += fee[0] * plan[j]
                plan[j] = 0
                swim(j+1)
                plan[j] = x
                total -= fee[0] * plan[j]
            elif i == 1:
                x = plan[j]
                plan[j] = 0
                total += fee[1]
                swim(j+1)
                plan[j] = x
                total -= fee[1]
            else:
                if j+1 < 12 and j+2 < 12:
                    x,y,z = plan[j],plan[j+1],plan[j+2]
                    plan[j],plan[j+1],plan[j+2] = 0,0,0
                    total += fee[2]
                    swim(j+1)
                    plan[j], plan[j+1], plan[j+2] = x,y,z
                    total -= fee[2]
                elif j+1 < 12:
                    x,y = plan[j],plan[j+1]
                    plan[j],plan[j+1] = 0,0
                    total += fee[2]
                    swim(j+1)
                    plan[j],plan[j+1] = x,y
                    total -= fee[2]
                else:
                    x = plan[j]
                    plan[j] = 0
                    total += fee[2]
                    swim(j+1)
                    plan[j] = x
                    total -= fee[2]
    elif plan[j] == 0:
        swim(j+1)

T = int(input())
for t in range(1, T + 1):
    fee = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    total = 0
    min_fee = 10000000000
    swim(0)
    if fee[3] < min_fee:
        min_fee = fee[3]
    print('#{} {}'.format(t,min_fee))
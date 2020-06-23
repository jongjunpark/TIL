T = int(input())
for t in range(1, T+1):
    num = list(map(int, input().split()))
    x1 = [1]
    a = 1
    for i in range(1,300):
        a += i
        x1.append(a)
    tmp = []
    for j in num:
        count = -1           #j = 6
        one = 1
        for i in x1:
            count += 1      #count = 3
            if i>j:         #7>6
                break
        n = j - x1[count-1] #count-1 = 2, x1[count-1] = 4
        for i in range(n):
           one += 1
           count -= 1
        tmp.append((one,count))
    x,y = 0,0
    for i in range(len(tmp)):
        x += tmp[i][0]
        y += tmp[i][1]
    count = 0
    while True:
        x -= 1
        y += 1
        count += 1
        if x == 1:
            break
    print(f'#{t} {x1[y-1]+count}')
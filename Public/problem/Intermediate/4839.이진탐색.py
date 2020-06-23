T = int(input())
for t in range(1, T + 1):
    data = list(map(int, input().split()))
    l = 1
    r = data[0]
    a = data[1]
    b = data[2]
    total1 = 0
    total2 = 0
    while True:
        c = int((l + r) / 2)
        total1 += 1
        if c > a:
            r = c
        else:
            l = c
        if c == a:
            break
    l = 1
    r = data[0]
    while True:
        c = int((l + r) / 2)
        total2 += 1
        if c > b:
            r = c
        else:
            l = c
        if c == b:
            break
    if total1 > total2:
        print(f'#{t} B')
    elif total2 > total1:
        print(f'#{t} A')
    else:
        print(f'#{t} 0')

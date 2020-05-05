T = int(input())
for t in range(1,T+1):
    time = list(map(int, input().split()))
    h = time[0] + time[2]
    if h>12:
        h = h - 12
    m = time[1] + time[3]
    if m>=60:
        m = m - 60
        h += 1
    print(f'#{t} {h} {m}')
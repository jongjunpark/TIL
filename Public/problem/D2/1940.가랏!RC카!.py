T = int(input())
for t in range(1, T + 1):
    N = int(input())
    data = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        data.append(tmp)
    velocity = 0
    meter = 0
    for i in range(len(data)):
        if velocity == 0 and data[i][0] == 2:
            continue
        else:
            if data[i][0] == 1:
                velocity += data[i][1]
                meter += velocity
            elif data[i][0] == 2:
                velocity -= data[i][1]
                meter += velocity
            else:
                meter += velocity

    print(f'#{t} {meter}')
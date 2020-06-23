T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    i, j, x, y = 0, 1, 0, 0
    while True:
        if arr[x][y] != 0:
            break
        arr[x][y] = j

        if N == 1:
            break

        dx, dy = delta[i]
        a = x + dx
        b = y + dy
        j += 1

        if a > len(arr) - 1 or b > len(arr[x]) - 1 or arr[a][b] != 0:
            i += 1
            if i == 4:
                i = 0
            dx, dy = delta[i]
            a = x + dx
            b = y + dy

        x = a
        y = b
    print(f'#{t}')
    for i in range(N):
        p = ' '.join(map(str, arr[i]))
        print(p)
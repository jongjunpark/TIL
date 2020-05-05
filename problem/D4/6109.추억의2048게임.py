T = int(input())
for t in range(1, T + 1):
    n, direction = map(str, input().split())
    N = int(n)
    arr = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        arr.append(tmp)

    if direction == 'up':
        for i in range(N):
            for j in range(N - 1):
                if arr[j][i] == 0:
                    k = 1
                    while j + k <= N - 1:
                        if arr[j + k][i] != 0:
                            arr[j][i], arr[j + k][i] = arr[j + k][i], arr[j][i]
                            break
                        k += 1
                if arr[j + 1][i] == 0:
                    k = 1
                    while j + 1 + k <= N - 1:
                        if arr[j + 1 + k][i] != 0:
                            arr[j + 1][i], arr[j + 1 + k][i] = arr[j + 1 + k][i], arr[j + 1][i]
                            break
                        k += 1
                if arr[j][i] == arr[j + 1][i]:
                    arr[j][i] = arr[j][i] * 2
                    arr[j + 1][i] = 0

    if direction == 'down':
        for i in range(N):
            for j in range(1, N):
                if arr[-j][i] == 0:
                    k = 1
                    while -j - k >= -N:
                        if arr[-j - k][i] != 0:
                            arr[-j][i], arr[-j - k][i] = arr[-j - k][i], arr[-j][i]
                            break
                        k += 1
                if arr[-j - 1][i] == 0:
                    k = 1
                    while -j - 1 - k >= -N:
                        if arr[-j - 1 - k][i] != 0:
                            arr[-j - 1][i], arr[-j - 1 - k][i] = arr[-j - 1 - k][i], arr[-j - 1][i]
                            break
                        k += 1
                if arr[-j][i] == arr[-j - 1][i]:
                    arr[-j][i] = arr[-j][i] * 2
                    arr[-j - 1][i] = 0

    if direction == 'left':
        for i in range(N):
            for j in range(N - 1):
                if arr[i][j] == 0:
                    k = 1
                    while j + k <= N - 1:
                        if arr[i][j + k] != 0:
                            arr[i][j], arr[i][j + k] = arr[i][j + k], arr[i][j]
                            break
                        k += 1
                if arr[i][j + 1] == 0:
                    k = 1
                    while j + 1 + k <= N - 1:
                        if arr[i][j + 1 + k] != 0:
                            arr[i][j + 1], arr[i][j + 1 + k] = arr[i][j + 1 + k], arr[i][j + 1]
                            break
                        k += 1
                if arr[i][j] == arr[i][j + 1]:
                    arr[i][j] = arr[i][j] * 2
                    arr[i][j + 1] = 0

    if direction == 'right':
        for i in range(N):
            for j in range(1, N):
                if arr[i][-j] == 0:
                    k = 1
                    while -j - k >= -N:
                        if arr[i][-j - k] != 0:
                            arr[i][-j], arr[i][-j - k] = arr[i][-j - k], arr[i][-j]
                            break
                        k += 1
                if arr[i][-j - 1] == 0:
                    k = 1
                    while -j - 1 - k >= -N:
                        if arr[i][-j - 1 - k] != 0:
                            arr[i][-j - 1], arr[i][-j - 1 - k] = arr[i][-j - 1 - k], arr[i][-j - 1]
                            break
                        k += 1
                if arr[i][-j] == arr[i][-j - 1]:
                    arr[i][-j] = arr[i][-j] * 2
                    arr[i][-j - 1] = 0
    print(f'#{t}')
    for i in range(len(arr)):
        a = ' '.join(map(str, arr[i]))
        print(a)

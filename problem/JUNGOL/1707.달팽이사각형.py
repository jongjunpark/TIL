n = int(input())
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
arr = []
for i in range(n):
    arr.append([0] * n)

i, j = 0, 0
k, t = 1, 0
if n == 1:
    print(1)
else:
    while True:
        if arr[i][j] != 0:
            break
        arr[i][j] = k
        dx, dy = delta[t]
        X = i + dx
        Y = j + dy
        if X < 0 or Y < 0 or X > n - 1 or Y > n - 1 or arr[X][Y] != 0:
            t += 1
            if t == 4:
                t = 0
            dx, dy = delta[t]
            X = i + dx
            Y = j + dy
        i = X
        j = Y
        k += 1
    for i in range(n):
        print(' '.join(map(str, arr[i])))
n = int(input())
arr = []
for i in range(n):
    tmp = [0] * n
    arr.append(tmp)
i, j = 0, n // 2
k = 1

while k <= n * n:
    arr[i][j] = k
    if k % n == 0:
        X = i + 1
    else:
        X = i - 1
        Y = j - 1
        if X < 0:
            X = n - 1
        if Y < 0:
            Y = n - 1
    i = X
    j = Y
    k += 1
for i in range(n):
    print(' '.join(map(str, arr[i])))
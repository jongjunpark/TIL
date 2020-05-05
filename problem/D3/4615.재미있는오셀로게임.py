T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        a = [0] * N
        arr.append(a)
    arr[N // 2 - 1][N // 2 - 1] = 2
    arr[N // 2][N // 2] = 2
    arr[N // 2][N // 2 - 1] = 1
    arr[N // 2 - 1][N // 2] = 1

    for i in range(M):
        x, y, c = map(int, input().split())
        a = x - 1
        b = y - 1

        tmp = []
        # 좌
        count = 0
        for i in range(1, N):
            if b - i < 0 or arr[a][b - i] == 0:
                break
            if arr[a][b - i] != 0 and arr[a][b - i] != c:
                count += 1
            if arr[a][b - i] == c:
                for i in range(1, count + 1):
                    tmp.append((a, b - i))
                break
        # 우
        count = 0
        for i in range(1, N):
            if b + i > N - 1 or arr[a][b + i] == 0:
                break
            if arr[a][b + i] != 0 and arr[a][b + i] != c:
                count += 1
            if arr[a][b + i] == c:
                for i in range(1, count + 1):
                    tmp.append((a, b + i))
                break

        # 상
        count = 0
        for i in range(1, N):
            if a - i < 0 or arr[a - i][b] == 0:
                break
            if arr[a - i][b] != 0 and arr[a - i][b] != c:
                count += 1
            if arr[a - i][b] == c:
                for i in range(1, count + 1):
                    tmp.append((a - i, b))
                break

        # 하
        count = 0
        for i in range(1, N):
            if a + i > N - 1 or arr[a + i][b] == 0:
                break
            if arr[a + i][b] != 0 and arr[a + i][b] != c:
                count += 1
            if arr[a + i][b] == c:
                for i in range(1, count + 1):
                    tmp.append((a + i, b))
                break
        # 좌상
        count = 0
        i = 1
        for i in range(1, N):
            if a - i < 0 or b - i < 0 or arr[a - i][b - i] == 0:
                break
            if arr[a - i][b - i] != 0 and arr[a - i][b - i] != c:
                count += 1
            if arr[a - i][b - i] == c:
                for j in range(1, count + 1):
                    tmp.append((a - j, b - j))
                break

        # 좌하
        count = 0
        for i in range(1, N):
            if a + i > N - 1 or b + i > N - 1 or arr[a + i][b + i] == 0:
                break
            if arr[a + i][b + i] != 0 and arr[a + i][b + i] != c:
                count += 1
            if arr[a + i][b + i] == c:
                for j in range(1, count + 1):
                    tmp.append((a + j, b + j))
                break

        # 우상
        count = 0
        for i in range(1, N):
            if a - i < 0 or b + i > N - 1 or arr[a - i][b + i] == 0:
                break
            if arr[a - i][b + i] != 0 and arr[a - i][b + i] != c:
                count += 1
            if arr[a - i][b + i] == c:
                for j in range(1, count + 1):
                    tmp.append((a - j, b + j))
                break

        # 우하
        count = 0
        for i in range(1, N):
            if a + i > N - 1 or b - i < 0 or arr[a + i][b - i] == 0:
                break
            if arr[a + i][b - i] != 0 and arr[a + i][b - i] != c:
                count += 1
            if arr[a + i][b - i] == c:
                for j in range(1, count + 1):
                    tmp.append((a + j, b - j))
                break

        arr[a][b] = c

        for x, y in tmp:
            if c == 1:
                arr[x][y] = 1
            else:
                arr[x][y] = 2

    one_count = 0
    two_count = 0
    for i in range(len(arr)):
        one_count += arr[i].count(1)
        two_count += arr[i].count(2)
    print(f'#{t} {one_count} {two_count}')
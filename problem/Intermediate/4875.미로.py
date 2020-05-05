def walk(i, j):
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    i, j = stack[-1]
    for k in range(4):
        dx, dy = delta[k]
        x = i + dx
        y = j + dy
        if 0 <= x < N and 0 <= y < N and data[x][y] == '3':
            return print('#{} 1'.format(t))
        if 0 <= x < N and 0 <= y < N and data[x][y] == '0' and (x, y) not in visited:
            stack.append((x, y))
            visited.append((x, y))
            walk(x, y)
    else:
        stack.pop()
        if len(stack) == 0:
            return print('#{} 0'.format(t))


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    stack = []
    visited = []
    data = []
    for i in range(N):
        tmp = input()
        l_tmp = []
        for j in range(N):
            l_tmp.append(tmp[j])
        data.append(l_tmp)
    for i in range(N):
        for j in range(N):
            if data[i][j] == '2':
                stack.append((i, j))
                walk(i, j)
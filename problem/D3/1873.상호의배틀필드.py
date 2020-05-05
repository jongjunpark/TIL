T = int(input())
for t in range(1, T+1):
    H, W = map(int, input().split())
    arr = []
    for i in range(H):
        st = input()
        tmp = []
        for j in st:
            tmp.append(j)
        arr.append(tmp)
    N = int(input())
    command = input()
    now = []
    s = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '<' or arr[i][j] == '>' or arr[i][j] == '^' or arr[i][j] == 'v':
                now.append(i)
                now.append(j)
                if arr[i][j] == '<':
                    s = 2
                elif arr[i][j] == '>':
                    s = 3
                elif arr[i][j] == '^':
                    s = 0
                else:
                    s = 1

    delta = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우

    for k in command:
        if k == 'R':
            s = 3
            if now[1]+1 < W and arr[now[0]][now[1]+1] == '.':
                arr[now[0]][now[1]] = '.'
                now[1] += 1
                arr[now[0]][now[1]] = '>'
            else:
                arr[now[0]][now[1]] = '>'

        elif k == 'L':
            s = 2
            if now[1]-1 >= 0 and arr[now[0]][now[1]-1] == '.':
                arr[now[0]][now[1]] = '.'
                now[1] -= 1
                arr[now[0]][now[1]] = '<'
            else:
                arr[now[0]][now[1]] = '<'

        elif k == 'U':
            s = 0
            if now[0]-1 >= 0 and arr[now[0]-1][now[1]] == '.':
                arr[now[0]][now[1]] = '.'
                now[0] -= 1
                arr[now[0]][now[1]] = '^'
            else:
                arr[now[0]][now[1]] = '^'

        elif k == 'D':
            s = 1
            if now[0]+1 < H and arr[now[0]+1][now[1]] == '.':
                arr[now[0]][now[1]] = '.'
                now[0] += 1
                arr[now[0]][now[1]] = 'v'
            else:
                arr[now[0]][now[1]] = 'v'
        if k == 'S':
            dx, dy = delta[s]
            x = now[0]
            y = now[1]
            while True:
                X = x + dx
                Y = y + dy
                if X < 0 or X >= H or Y < 0 or Y >= W:
                    break
                if arr[X][Y] == '#':
                    break
                else:
                    if arr[X][Y] == '*':
                        arr[X][Y] = '.'
                        break
                x = X
                y = Y
    print('#{}'.format(t),end=' ')
    for i in range(H):
        print(''.join(arr[i]))

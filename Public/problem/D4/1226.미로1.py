T = 10
for t in range(1,T+1):
    case = int(input())
    arr = []
    for i in range(16):
        a = input()
        tmp = []
        for j in range(16):
            tmp.append(int(a[j]))
        arr.append(tmp)
    delta = [(0,-1),(0,1),(1,0),(-1,0)]    #좌우하상

    stack = []
    stack.append((1,1))
    visited = []
    for l in range(16):
        tmp = [0]*16
        visited.append(tmp)
    j = 1
    i = 1
    count = 0
    while len(stack) > 0:
        for k in range(4):
            i,j = stack[-1]
            dx, dy = delta[k]
            X = i + dx
            Y = j + dy
            if 0 <= X <= 15 and 0 <= Y <= 15 and (arr[X][Y] == 0 or arr[X][Y] == 2) and visited[X][Y] == 0:
                i,j = X,Y
                stack.append((i,j))
                visited[i][j] = 1
                break
            elif 0 <= X <= 15 and 0 <= Y <= 15 and arr[X][Y] == 3:
                count += 1
        else:
            stack.pop()
    if count > 0:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))
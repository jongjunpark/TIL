T = 10
for t in range(1,T+1):
    test = int(input())
    arr = []
    for i in range(100):
        tmp = list(map(int,input().split()))
        arr.append(tmp)

    start = []
    count = 0
    for i in range(100):
        if arr[0][i] == 1:
            start.append(count)
        count += 1

    delta = [(0,-1),(0,1),(1,0)]    #좌우하

    min_count = 100000
    idx = 0
    for i in range(len(start)):
        stack = []
        stack.append((0,start[i]))
        a = i
        b = start[i]
        visited = []
        for l in range(100):
            tmp = [0]*100
            visited.append(tmp)
        j = 0
        count = 0
        while len(stack) > 0:
            for k in range(3):
                dx, dy = delta[k]
                X = j + dx
                Y = b + dy
                if 0 <= X <= 99 and 0 <= Y <= 99 and arr[X][Y] == 1 and visited[X][Y] == 0:
                    j,b = X,Y
                    stack.append((j,b))
                    visited[j][b] = 1
                    break
                elif 0 <= X <= 99 and 0 <= Y <= 99 and arr[X][Y] == 2:
                    count += 1
            else:
                stack.pop()
        if count > 0:
            print('#{} {}'.format(t,start[i]))
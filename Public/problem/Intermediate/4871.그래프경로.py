T = int(input())
for t in range(1, T+1):
    v, e = map(int,input().split())
    point = []
    for i in range(e):
        tmpa,tmpb = map(int,input().split())
        point.append(tmpa)
        point.append(tmpb)
    s, g = map(int,input().split())
    stack = []
    visited = [0]*(v+1)


    # 인접행렬 제작
    mat = [[0]*(v+1) for _ in range(v+1)]
    for i in range(0,len(point),2):
        a,b = point[i], point[i+1]
        mat[a][b] = 1

    stack.append(s)

    while len(stack) > 0:
        if stack[-1] == g:
            print('#{} 1'.format(t))
            break

        current = stack[-1]
        visited[current] = 1
        for i in range(len(mat[current])):
            if mat[current][i] == 1 and visited[i] == 0:
                stack.append(i)
                break
        else:
            stack.pop()
    if len(stack) == 0:
        print('#{} 0'.format(t))

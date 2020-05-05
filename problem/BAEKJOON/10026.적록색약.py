N = int(input())
data = []
for i in range(N):
    tmp = input()
    tmp_list = []
    for j in tmp:
        tmp_list.append(j)
    data.append(tmp_list)

visited = [[0]*N for _ in range(N)]
delta = [(1,0),(0,1),(-1,0),(0,-1)]
counting = []
stack = []
count = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            stack.append((i,j))
            while len(stack) > 0:
                for k in range(4):
                    i,j = stack[-1]
                    dx,dy = delta[k]
                    X = i+dx
                    Y = j+dy
                    if 0 <= X < N and 0 <= Y < N and visited[X][Y] == 0 and data[X][Y] == data[i][j]:
                        stack.append((X,Y))
                        visited[X][Y] = 1
                        i,j = X,Y
                        break
                else:
                    stack.pop()
            count += 1
print(count, end=' ')

for i in range(N):
    for j in range(N):
        if data[i][j] == 'R':
            data[i][j] = 'G'
visited = [[0]*N for _ in range(N)]
delta = [(1,0),(0,1),(-1,0),(0,-1)]
counting = []
stack = []
count = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            stack.append((i,j))
            while len(stack) > 0:
                for k in range(4):
                    i,j = stack[-1]
                    dx,dy = delta[k]
                    X = i+dx
                    Y = j+dy
                    if 0 <= X < N and 0 <= Y < N and visited[X][Y] == 0 and data[X][Y] == data[i][j]:
                        stack.append((X,Y))
                        visited[X][Y] = 1
                        i,j = X,Y
                        break
                else:
                    stack.pop()
            count += 1
print(count)
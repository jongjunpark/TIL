N = int(input())
data = []
for i in range(N):
    tmp = input()
    tmp_list = []
    for j in tmp:
        tmp_list.append(int(j))
    data.append(tmp_list)

visited = [[0]*N for _ in range(N)]
delta = [(1,0),(0,1),(-1,0),(0,-1)]
start = []
counting = []
stack = []
for k in range(N):
    for l in range(N):
        if data[k][l] == 1:
            start.append((k,l))

for m in start:
    x,y = m
    if visited[x][y] == 0:
        count = 0
        stack.append((x,y))
        while len(stack) > 0:
            for k in range(4):
                i,j = stack[-1]
                dx,dy = delta[k]
                X = i+dx
                Y = j+dy
                if 0 <= X < N and 0 <= Y < N and visited[X][Y] == 0 and data[X][Y] == 1:
                    stack.append((X,Y))
                    count += 1
                    visited[X][Y] = 1
                    i,j = X,Y
                    break
            else:
                stack.pop()

        counting.append(count)
counting.sort()
print(len(counting))
for i in counting:
    if i == 0:
        print(1)
    else:
        print(i)
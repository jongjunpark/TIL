def BFS():
    global flag, result
    while q:
        t = q.pop(0)
        if graph[t] == []:
            result += 1
            return
        for k in graph[t]:
            if visited[k] == 0:
                flag = True
                q.append(k)
                visited[k] = 1
    if flag:
        result += 1
    return

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
result = 0
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (N+1)
for i in range(1,N+1):
    flag = False
    q = []
    q.append(i)
    visited[i] = 1
    BFS()
print(result)
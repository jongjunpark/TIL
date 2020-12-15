def DFS():
    while stack:
        t = stack[-1]
        for i in graph[t]:
            if visited[i] == 0:
                stack.append(i)
                stack_result.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()
    return

def BFS():
    while q:
        t = q.pop(0)
        for i in graph[t]:
            if visited[i] == 0:
                q.append(i)
                q_result.append(i)
                visited[i] = 1
    return

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for k in range(N+1):
    graph[k].sort()
stack = []
stack_result = []
q = []
q_result = []
stack.append(V)
stack_result.append(V)
q.append(V)
q_result.append(V)
visited = [0] * (N + 1)
visited[V] = 1
DFS()
visited = [0] * (N + 1)
visited[V] = 1
BFS()
print(' '.join(map(str,stack_result)))
print(' '.join(map(str,q_result)))
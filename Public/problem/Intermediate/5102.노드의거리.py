def BFS(S,graph, G):
    queue.append(S)
    visited[S] = 0
    while queue:
        t = queue.pop(0)
        for i in graph[t]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[t] + 1
                if i == G:
                    return print("#{} {}".format(tc,visited[t]+1))
    return print("#{} 0".format(tc))

for tc in range(1,int(input())+1):
    V, E  = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    S, G = map(int, input().split())
    queue = []
    visited = [0] * (V+1)
    BFS(S, graph, G)
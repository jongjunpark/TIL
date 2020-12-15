def DFS():
    t = visited[-1]
    while stack:
        for i in graph[t]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                if t in left:
                    right.append(i)
                else:
                    left.append(i)
                return
        else:
            stack.pop()
    return

def Bipartite():
    for i in left:
        for j in range(len(graph[i])):
            if graph[i][j] in left:
                return print("NO")
    for i in right:
        for j in range(len(graph[i])):
            if graph[i][j] in right:
                return print("NO")
    return print("YES")

T = int(input())
for _ in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [0] * (V+1)
    left = []
    right = []
    for i in range(1, V+1):
        flag = False
        stack = []
        stack.append(i)
        visited[i] = 1
        for j in graph[i]:
            if j in left:
                flag = True
        if flag == False:
            left.append(i)
        else:
            right.append(i)
        DFS()
    Bipartite()









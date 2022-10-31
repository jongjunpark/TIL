
from collections import defaultdict, deque

def bfs(n, tree_graph, start, end, isFinish=False):
    visted = [0] * (n+1)
    queue = deque([start])
    visted[start] = 1

    while queue:
        node = queue.popleft()
        path_length = visted[node]

        for i in tree_graph[node]:
            if i == end:
                return path_length
            if visted[i] == 0 and (isFinish or i != n):
                queue.append(i)
                visted[i] = path_length + 1
    else:
        return float('inf')

def minimumTreePath(n, edges, visitNodes):
    # Write your code here
    tree_graph = defaultdict(list)
    
    for edge in edges:
        # 딕셔너리 key -> 시작노드, value -> [도착노드, 방문여부] 방문여부는 0: 미방문, 1: 방문
        tree_graph[edge[0]].append(edge[1])
        tree_graph[edge[1]].append(edge[0])
  
    min_result = float('inf')

    stack = []

    for i in range(len(visitNodes)):
        visited = [False]*len(visitNodes)
        stack.append((1,visitNodes[i]))
        visited[i] = True

        result = 0

        while stack:
            start, end = stack.pop()
            result += bfs(n, tree_graph, start, end)
            for i in range(len(visitNodes)):
                if not visited[i]:
                    stack.append((end, visitNodes[i]))
                    visited[i] = True

        result += bfs(n, tree_graph, end, n, True)

        if result < min_result:
            min_result = result
            

    return min_result

    

print(minimumTreePath(5, [[1, 2], [1, 3], [3,4], [3,5]], [2,4]))

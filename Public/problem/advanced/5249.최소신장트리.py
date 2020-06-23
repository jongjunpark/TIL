import heapq

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V+1)}
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])
        adj[e].append([s, c])

    # result = 0
    # for i in range(V+1):
    INF = float('inf')
    key = [INF] * (V + 1)
    mst = [False] * (V + 1)
    pq = []
    key[0] = 0
    heapq.heappush(pq, (0, 0))
    result = 0
    while pq:
        min_key, node = heapq.heappop(pq)
        if mst[node]:
            continue
        mst[node] = True
        result += min_key

        for dest, wt in adj[node]:
            if not mst[dest] and key[dest] > wt:
                key[dest] = wt
                heapq.heappush(pq, (key[dest], dest))
    print('#{} {}'.format(tc,result))
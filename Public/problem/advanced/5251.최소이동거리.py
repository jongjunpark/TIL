def dist(node, t):
    global min_dist
    if t > min_dist:
        return
    if node == N:
        min_dist = t
        return
    for i in range(len(adj[node])):
        dist(adj[node][i][0], t+adj[node][i][1])

for tc in range(1, int(input())+1):
    N, E = map(int,input().split())
    adj = {i: [] for i in range(N)}
    for i in range(E):
        s,e,w = map(int,input().split())
        adj[s].append([e,w])
    # print(adj)
    min_dist = float('inf')
    for i in range(len(adj[0])):
        dist(adj[0][i][0], adj[0][i][1])
    print('#{} {}'.format(tc,min_dist))
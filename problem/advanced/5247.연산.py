for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    queue = [0]*1000001
    front, rear = -1, 0
    dist = [0]*1000001
    visited = [0]*1000001
    queue[0] = N
    while front != rear:
        front += 1
        x = queue[front]
        d = dist[front]
        visited[x] = 1
        if x == M:
            break
        for i in range(4):
            if i == 0:
                if x+1 < 1000000 and visited[x+1] == 0 and rear < 1000000:
                    rear += 1
                    queue[rear] = x+1
                    dist[rear] = d+1
            elif i == 1:
                if x-1 > 0 and visited[x-1] == 0 and rear < 1000000:
                    rear += 1
                    queue[rear] = x-1
                    dist[rear] = d+1
            elif i == 2:
                if x*2 < 1000000 and visited[x*2] == 0 and rear < 1000000:
                    rear += 1
                    queue[rear] = x*2
                    dist[rear] = d+1
            else:
                if x-10 > 0 and visited[x-10] == 0 and rear < 1000000:
                    rear += 1
                    queue[rear] = x-10
                    dist[rear] = d+1

    print('#{} {}'.format(tc,max(dist)-1))
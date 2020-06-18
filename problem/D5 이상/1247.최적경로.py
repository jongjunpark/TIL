def dist_customer(a, b, dist, cnt):
    global min_dist
    if dist >= min_dist:
        return
    if cnt == N:
        result = dist+abs(customer[a]-home[0])+abs(customer[b]-home[1])
        if result < min_dist:
            min_dist = result
        return
    for i in range(len(customer)//2):
        if visited[i] == 0:
            visited[i] = 1
            dist_customer(i*2, i*2+1, dist+abs(customer[a]-customer[i*2])+abs(customer[b]-customer[i*2+1]), cnt+1)
            visited[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    data = list(map(int,input().split()))
    company = [data[0],data[1]]
    home = [data[2],data[3]]
    customer = data[4:]
    visited = [0]*N
    min_dist = float('inf')
    for i in range(len(customer)//2):
        visited[i] = 1
        dist_customer(i*2, i*2+1, abs(company[0]-customer[i*2])+abs(company[1]-customer[i*2+1]), 1)
        visited[i] = 0
    print('#{} {}'.format(tc,min_dist))
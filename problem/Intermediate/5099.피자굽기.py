for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    cheeze = list(map(int,input().split()))
    oven = [0] * N
    idx = [0] * N
    rear = 0
    front = 0
    while True:
        oven[front] //= 2
        if oven[front] == 0 and rear < M:
            oven[front] = cheeze[rear]
            idx[front] = rear
            rear += 1
            front = (front + 1) % N
        elif oven[front] == 0:
            oven[front] = 0
            front = (front + 1) % N
            if oven.count(0) == N - 1:
                break
        else:
            front = (front + 1) % N
    for i in range(N):
        if oven[i] != 0:
            print('#{} {}'.format(tc,idx[i]+1))
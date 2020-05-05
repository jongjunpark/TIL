def max_prob(i, s):
    global maximum
    if i == N:
        if s > maximum:
            maximum = s
        return
    if s <= maximum:
        return

    for x in range(N):
        if check[x] == 0:
            check[x] = 1
            max_prob(i + 1, s*(prob[i][x]/100))
            check[x] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    prob = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*N
    maximum = 0
    max_prob(0, 1)
    print('#{} {:0.6f}'.format(t,round(maximum*100,6)))
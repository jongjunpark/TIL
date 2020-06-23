T = int(input())
for t in range(1, T + 1):
    N = int(input())
    score = list(map(int,input().split()))
    result = {0}
    for i in range(N):
        tmp = set()
        for j in result:
            tmp.add(j+score[i])
        result |= tmp

    print('#{} {}'.format(t,len(result)))
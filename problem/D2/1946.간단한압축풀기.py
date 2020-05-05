T = int(input())
for t in range(1,T+1):
    N = int(input())
    data = []
    for i in range(N):
        tmp = list(map(str, input().split()))
        data.append(tmp)
    tmp = ''
    for i in range(len(data)):
        tmp += (data[i][0] * int(data[i][1]))
    i = 0
    print(f'#{t}')
    while i < len(tmp) - 1:
        print(tmp[i:10+i])
        i += 10
T = int(input())
for t in range(1,T+1):
    N = int(input())
    farm = []
    for i in range(N):
        tmp = input()
        farm.append(tmp)
    result = 0
    for i in range(N):
        j = 0
        if i <= int(N/2):
            while j <= i:
                result += int(farm[int(N/2)+j][i])
                if j != 0:
                    result += int(farm[int(N/2)-j][i])
                j += 1
        else:
            while j < N-i:
                result += int(farm[int(N/2)+j][i])
                if j != 0:
                    result += int(farm[int(N/2)-j][i])
                j += 1
    print('#{} {}'.format(t, result))
T = 10
for t in range(1,T+1):
    N = int(input())
    arr = []
    for i in range(N):
        num = list(map(int,input().split()))
        arr.append(num)
    result = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[j][i] == 1 and count == 0:
                count += 1
            if arr[j][i] == 2 and count == 0:
                arr[j][i] = 0
            if j+1 <= N-1 and arr[j][i] == 1 and arr[j+1][i] != 2:
                arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            if j+1 <= N-1 and arr[j][i] == 1 and arr[j+1][i] == 2:
                result += 1
    print('#{} {}'.format(t,result))

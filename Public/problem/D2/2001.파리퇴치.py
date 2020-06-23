T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    numbers = []
    for i in range(N):
        number = list(map(int,input().split()))
        numbers.append(number)
    max_num = 0
    for i in range(len(numbers)-M+1):
        for j in range(len(numbers)-M+1):
            result = 0
            for k in range(M):
                for l in range(M):
                    result += numbers[i+l][j+k]
            if result > max_num:
                max_num = result
    print(f'#{t} {max_num}')
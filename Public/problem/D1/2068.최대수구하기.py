T = int(input())
for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    result = 0
    for i in numbers:
        if i > result:
            result = i
    print(f'#{t} {result}')
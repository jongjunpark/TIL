T = int(input())
for t in range(1,T+1):
    count = int(input())
    numbers = list(map(int,input().split()))

    for j in range(len(numbers)-1):
        for i in range(len(numbers)-j-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    a = ' '.join(map(str, numbers))
    print(f'#{t} {a}')

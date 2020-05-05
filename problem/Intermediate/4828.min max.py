T = int(input())
for t in range(1,T+1):
    length = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    i = 1
    for x in range(length[0]):
        for n in range(length[0]-i):
            if numbers[n] > numbers[n+1]:
                a = numbers[n+1]
                numbers[n+1] = numbers[n]
                numbers[n] = a
    result = numbers[-1] - numbers[0]
    print("#{0} {1}".format(t, result))
T = int(input())
for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    total = 0

    for j in numbers:
        if j % 2 != 0:
            total += j

    print("#{} {}".format(t,total))
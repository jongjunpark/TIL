T = int(input())
for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    total = 0

    for j in numbers:
        total += j

    print("#{} {}".format(t,round(total/len(numbers))))
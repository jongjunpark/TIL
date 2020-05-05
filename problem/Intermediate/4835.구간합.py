T = int(input())
for t in range(1,T+1):
    data = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    blank = []
    for i in range(data[0]-data[1]+1):
        result = 0
        result += numbers[i]
        for j in range(1,data[1]):
            result += numbers[i+j]
        blank.append(result)
    a = max(blank) - min(blank)
    print("#{0} {1}".format(t,a))
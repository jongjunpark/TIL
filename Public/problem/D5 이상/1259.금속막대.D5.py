T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    list1 = []
    for n in range(0,len(num),2):
        list1.append([num[n], num[n+1]])
    res = []
    for k in list1:
        b = []
        b.append(k)
        for j in range(len(list1)):
            for i in range(len(list1)):
                if b[-1][1] == list1[i][0]:
                    b.append(list1[i])
                    break
        if len(b) > len(res):
            res = b
    print(f'#{t}',end=' ')
    for i in range(len(res)):
        for j in range(2):
            print(res[i][j],end=' ')
    print('')
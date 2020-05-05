T = int(input())
for t in range(1, T+1):
    N = int(input())
    list1 = []
    list2 = []
    for n in range(N):
        number = list(map(int, input().split()))
        if number[4] == 1:
            list1.append(number)
        else:
            list2.append(number)
    blank1 = {0}
    blank2 = {1}
    for x in range(len(list1)):
        for i in range(list1[x][2]-list1[x][0]+1):
            for j in range(list1[x][3]-list1[x][1]+1):
                blank1.update({(list1[x][0]+i, list1[x][1]+j)})
    for x in range(len(list2)):
        for i in range(list2[x][2]-list2[x][0]+1):
            for j in range(list2[x][3]-list2[x][1]+1):
                blank2.update({(list2[x][0]+i, list2[x][1]+j)})
    total = 0
    for i in blank1:
        if i in blank2:
            total += 1
    print(f'#{t} {total}')
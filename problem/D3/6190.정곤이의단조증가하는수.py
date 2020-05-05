T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    blank = []
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            blank.append(str(num[j] * num[i]))
    max_num = 0
    count = 0
    for i in range(len(blank)):
        count = 0
        if len(blank[i]) <= 1:
            count += 1
        for j in range(len(blank[i]) - 1):
            if blank[i][j] > blank[i][j + 1]:
                count += 1
        if count == 0 and int(blank[i]) > max_num and int(blank[i]) % 11 != 0:
            max_num = int(blank[i])
    if max_num != 0:
        print(f'#{t} {max_num}')
    else:
        print(f'#{t} -1')

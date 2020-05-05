T = int(input())
for t in range(1, T+1):
    num = list(map(int,input().split()))

    sum_list = []

    for i in range(5):
        for j in range(i+1,6):
            for k in range(j+1,7):
                if num[i]+num[j]+num[k] not in sum_list:
                    sum_list.append(num[i]+num[j]+num[k])
    sum_list.sort()
    print('#{} {}'.format(t,sum_list[-5]))
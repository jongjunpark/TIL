def change_num(num_list, cnt):
    global max_result
    if cnt == times:
        return
    for i in range(k-1):
        for j in range(i+1,k):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            result = int(''.join(map(str,num_list)))
            if result in f[cnt+1]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
                continue
            else:
                f[cnt+1].append(result)
                change_num(num_list, cnt+1)
                num_list[i],num_list[j] = num_list[j],num_list[i]


for tc in range(1, int(input())+1):
    num, times = map(int, input().split())
    num_str = str(num)
    num_list = []
    for i in num_str:
        num_list.append((int(i)))
    k = len(num_list)
    max_result = 0
    f = {i: [] for i in range(times+1)}
    f[0].append(num)
    change_num(num_list, 0)
    print('#{} {}'.format(tc,max(f[times])))
T = int(input())
for t in range(1, T+1):
    case = int(input())
    num = list(map(int, input().split()))
    total = 0
    max_num = 0
    for i in range(-1,-len(num)-1,-1):
        if num[i] < max_num:
            total += (max_num - num[i])
            i -= 1
        elif num[i] > max_num:
            max_num = num[i]
            i -= 1
    print(f'#{t} {total}')

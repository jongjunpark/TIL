T = int(input())
for t in range(1,T+1):
    number = list(map(int,input().split()))
    max_num = 0
    min_num = 100000
    result = 0
    for i in number:
        if i > max_num:
            max_num = i
        elif i < min_num:
            min_num = i
    number.remove(max_num)
    number.remove(min_num)
    for i in number:
        result += i
    print(f'#{t} {round(result/len(number))}')
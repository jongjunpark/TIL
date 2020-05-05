T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    number = []
    for i in range(2):
        num = list(map(int,input().split()))
        number.append(num)
    if len(number[0])>len(number[1]):
        number[0], number[1] = number[1], number[0]

    max_num = 0
    j = 0
    while j < len(number[1])-len(number[0])+1:
        result = 0
        for i in range(len(number[0])):
            result += number[0][i] * number[1][i+j]

        if result > max_num:
            max_num = result
        j += 1
    print(f'#{t} {max_num}')
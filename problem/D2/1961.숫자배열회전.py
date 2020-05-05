T = int(input())
for t in range(1,T+1):
    N = int(input())
    number = []
    for i in range(N):
        num = list(map(int, input().split()))
        number.append(num)
    a,b,c = '','',''
    result = []
    print(f'#{t}')
    for i in range(len(number)):
        for j in range(len(number[i])):
            a += str(number[-j-1][i])
            b += str(number[-i-1][-j-1])
            c += str(number[j][-i-1])
        print(''.join(a),end=' ')
        print(''.join(b),end=' ')
        print(''.join(c),end=' ')
        print()
        a,b,c = '','',''
for t in range(1, 11):
    N, num = map(str,input().split())
    N = int(N)
    number = []
    for i in range(N):
        number.append(num[i])

    for i in range(N):
        a = len(number)
        for j in range(a-1):
            if number[j] == number[j+1]:
                del number[j:j+2]
                break
    x = ''.join(number)
    print('#{} {}'.format(t,x))
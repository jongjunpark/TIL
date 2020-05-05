for t in range(1, int(input())+1):
    n, octa = map(str, input().split())
    N = int(n)
    result = ''
    for i in octa:
        tmp = int(i, 16)
        # result += bin(tmp) + ' '
        tmp2 = bin(tmp)
        if len(tmp2) < 6:
            result += '0' * (6-len(tmp2)) + tmp2[2:]
        else:
            result += tmp2[2:]

    print('#{} {}'.format(t,result))

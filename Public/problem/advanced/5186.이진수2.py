for t in range(1, int(input())+1):
    n = float(input())
    result = ''
    for i in range(1, 13):
        if n == 0:
            break
        if (n - 2 ** (-i)) >= 0:
            result += '1'
            n -= 2 ** (-i)
        else:
            result += '0'
    if n > 0:
        print('#{} overflow'.format(t))
    else:
        print('#{} {}'.format(t, result))
T = int(input())
for t in range(1, T+1):
    N = int(input())
    res = N ** (1/3)
    result = round(res)
    k = abs(res - result)
    if k < 0.00000001:
        print('#{} {}'.format(t,result))
    else:
        print('#{} -1'.format(t))
for tc in range(1, int(input())+1):
    p, q = map(float,input().split())
    P = (1-p)
    Q = (1-q)
    # 2, 틀 - 옳
    s1 = P * q
    # 3, 옳 - 틀 - 옳
    s2 = p * Q * q

    if s1 < s2:
        print('#{} YES'.format(tc))
    else:
        print('#{} NO'.format(tc))
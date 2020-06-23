h, type_num = map(int, input().split())
if 0 >= h or h > 100 or type_num < 1 or type_num > 3:
    print('INPUT ERROR!')
else:
    if type_num == 1:
        i = 1
        while i <= h:
            print('*' * i)
            i += 1

    elif type_num == 2:
        i = 0
        while i < h:
            print('*' * (h - i))
            i += 1

    else:
        i = 1
        j = h - 1
        while j >= 0:
            print(' ' * j + '*' * i)
            i += 2
            j -= 1
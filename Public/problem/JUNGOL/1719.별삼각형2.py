h, type_num = map(int, input().split())
if 0 >= h or h > 100 or type_num < 1 or type_num > 4 or h % 2 == 0:
    print('INPUT ERROR!')
else:
    if type_num == 1:
        i = 1
        while i <= int(h / 2) + 1:
            print('*' * i)
            i += 1
        i = 1
        while i < int(h / 2) + 1:
            print('*' * (int(h / 2) + 1 - i))
            i += 1

    elif type_num == 2:
        i = 1
        j = int(h / 2)
        while j >= 0:
            print(' ' * j + '*' * i)
            i += 1
            j -= 1
        i = int(h / 2)
        j = 1
        while i > 0:
            print(' ' * j + '*' * i)
            i -= 1
            j += 1

    elif type_num == 3:
        i = h
        j = 0
        while i > 0:
            print(' ' * j + '*' * i)
            i -= 2
            j += 1
        i = 3
        j = int(h / 2) - 1
        while i <= h:
            print(' ' * j + '*' * i)
            i += 2
            j -= 1
    else:
        i = int(h / 2) + 1
        j = 0
        while i > 0:
            print(' ' * j + '*' * i)
            i -= 1
            j += 1
        i = 2
        j = int(h / 2)
        while i <= int(h / 2) + 1:
            print(' ' * j + '*' * i)
            i += 1
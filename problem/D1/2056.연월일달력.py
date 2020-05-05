T = int(input())
for t in range(1, T+1):
    num = input()
    blank = []
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [4, 6, 9, 11]
    for i in num[0:4]:
        blank.append(i)
        year = ''.join(blank)
    blank = []
    for i in num[4:6]:
        blank.append(i)
        months = ''.join(blank)
        month = int(months)
    blank = []
    for i in num[6:]:
        blank.append(i)
        days = ''.join(blank)
        day = int(days)
    if month == 0 or day == 0:
        print(f'#{t} -1')
    elif month == 2 and day > 28:
        print(f'#{t} -1')
    elif month in month_31 and day > 31:
        print(f'#{t} -1')
    elif month in month_30 and day > 30:
        print(f'#{t} -1')
    else:
        print(f'#{t} {year}/{months}/{days}')
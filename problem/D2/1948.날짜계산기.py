T = int(input())
for t in range(1, T + 1):
    date = list(map(int, input().split()))
    day31 = [1, 3, 5, 7, 8, 10, 12]
    count = 0
    for i in range(date[0], date[2]):
        if i in day31:
            count += 1
    if date[0] > 2:
        result = (date[2] - date[0]) * 30 + (date[3] - date[1]) + 1 + count
    elif date[0] <= 2 and date[2] > 2:
        result = (date[2] - date[0]) * 30 + (date[3] - date[1]) + 1 + count - 2
    print(f'#{t} {result}')


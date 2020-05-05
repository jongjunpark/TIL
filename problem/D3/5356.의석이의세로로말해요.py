
T = int(input())
for t in range(1, T+1):
    data = []
    for i in range(5):
        a = input()
        data.append(a)
    max_len = 0
    for i in range(len(data)):
        if len(data[i]) > max_len:
            max_len = len(data[i])

    result = []
    i = 0
    while i <= max_len:
        for j in range(len(data)):
            if i >= len(data[j]):
                continue
            result.append(data[j][i])
        i += 1

    a = ''.join(result)
    print(f'#{t} {a}')
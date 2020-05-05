T = int(input())
for t in range(1,T+1):
    n = int(input())
    data = list(map(int,input().split()))
    blank = []
    for i in range(5):
        blank.append(str(max(data)))
        data.remove(max(data))
        blank.append(str(min(data)))
        data.remove(min(data))
        if len(data) == 0:
            break
    a = ' '.join(blank)
    print(f'#{t} {a}')
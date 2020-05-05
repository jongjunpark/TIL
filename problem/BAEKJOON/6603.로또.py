def power_set(selected, idx):
    if idx == N:
        if selected.count(1) == 6:
            for i in range(N):
                if selected[i] == 1:
                    print(data[i],end=' ')
            print()
        return
    selected[idx] = 1
    power_set(selected, idx+1)
    selected[idx] = 0
    power_set(selected, idx+1)


while True:
    tmp = list(map(int, input().split()))
    if len(tmp) == 1:
        break
    else:
        N = tmp[0]
        selected = [0]*N
        data = tmp[1:]
        power_set(selected,0)
    print()
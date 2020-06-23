def power_set(selected, idx):
    global result
    if len(result) > 0:
        return
    if idx == 9:
        total = 0
        if selected.count(1) == 7:
            for i in range(9):
                if selected[i] == 1:
                    total += data[i]
            if total == 100:
                for j in range(9):
                    if selected[j] == 1:
                        result.append(data[j])
        return
    selected[idx] = 1
    power_set(selected, idx+1)
    selected[idx] = 0
    power_set(selected, idx+1)


data = [int(input()) for _ in range(9)]
selected = [0] * 10
result = []
power_set(selected,0)
result.sort()
for k in result:
    print(k)
T = int(input())
for t in range(1,T+1):
    data = input()
    cards = []
    for i in range(int(len(data)/3)):
        a = ''
        for j in range(3):
            a += data[3*i+j]
        cards.append(a)
        count = 0
        for i in cards:
            for j in cards:
                if i == j:
                    count += 1
    S_count = 0
    D_count = 0
    H_count = 0
    C_count = 0
    if count > len(data)/3:
        print(f'#{t} ERROR')
    else:
        for i in cards:
            if 'S' in i:
                S_count += 1
            if 'D' in i:
                D_count += 1
            if 'H' in i:
                H_count += 1
            if 'C' in i:
                C_count += 1
        print(f'#{t} {13-S_count} {13-D_count} {13-H_count} {13-C_count}')
T = int(input())
for t in range(1,T+1):
    n = int(input())
    count = [0]*5
    while True:
        if n % 11 == 0:
            count[4] += 1
            n = int(n/11)
        elif n % 7 == 0:
            count[3] += 1
            n = int(n/7)
        elif n % 5 == 0:
            count[2] += 1
            n = int(n/5)
        elif n % 3 == 0:
            count[1] += 1
            n = int(n/3)
        elif n % 2 == 0:
            count[0] += 1
            n = int(n/2)
        else:
            break
    a = ' '.join(map(str,count))
    print(f'#{t} {a}')
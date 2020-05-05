T = int(input())
for t in range(1,T+1):
    data = input()
    count = 0
    tmp = ''
    while True:
        tmp += data[count]
        if tmp == data[count+1:(count+1)*2]:
            break
        count += 1
    print(f'#{t} {count+1}')
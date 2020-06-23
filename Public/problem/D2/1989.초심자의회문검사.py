T = int(input())
for t in range(1,T+1):
    a = input()
    list_a = list(a)
    blank = []
    while len(list_a):
        b = list_a.pop()
        blank.append(b)
    c = ''.join(blank)
    if a == c:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
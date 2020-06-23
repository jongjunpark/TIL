inp = int(input())
i = 1
while i <= inp:
    if inp % i == 0:
        print(i,end=' ')
    i += 1
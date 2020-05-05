T = int(input())
for t in range(1,T+1):
    D, A, B, F = map(int,input().split()) # D = 거리, A = a속력, B = b속력, F = 파리속도


    total = 0
    while True:
        # A -> B
        h = D/(B+F)
        total += F * h
        distance_A = A * h
        distance_B = B * h
        D -= (distance_A + distance_B)
        if D < 10**(-10):
            break
        # B -> A
        h = D/(A+F)
        total += F * h
        distance_A = A * h
        distance_B = B * h
        D -= (distance_A + distance_B)
        if D < 10**(-10):
            break
    print('#{} {}'.format(t,total))
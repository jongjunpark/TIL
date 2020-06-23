T = int(input())
for t in range(1, T+1):
    N = int(input())
    if N % 2 == 0:
        print('#{} Even'.format(t))
    else:
        print('#{} Odd'.format(t))
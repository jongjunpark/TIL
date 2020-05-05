T = int(input())
for t in range(1,T+1):
    N = input()
    M = input()
    for j in range(len(M)-len(N)+1):
        count = 0
        for i in range(len(N)):
            if N[i] == M[i+j]:
                count += 1
        if count == len(N):
            print('#{} 1'.format(t))
            break
    else:
        print('#{} 0'.format(t))
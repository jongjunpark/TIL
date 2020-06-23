T = int(input())
for t in range(1,T+1):
    N = int(input())
    A = []
    B = []

    for i in range(N):
        ai , bi = map(int,input().split())
        A.append(ai)
        B.append(bi)

    P = int(input())
    C = [int(input()) for _ in range(P)]
    D = list(set(C))
    count = [0]*(max(C)+1)


    for i in range(N):
        for j in range(len(D)):
            k = 0
            while A[i]+k <= B[i]:
                if A[i]+k == D[j]:
                    count[D[j]] += 1
                k += 1

    result = ''
    for x in range(P):
        result += str(count[C[x]]) + ' '

    print('#{} {}'.format(t,result))
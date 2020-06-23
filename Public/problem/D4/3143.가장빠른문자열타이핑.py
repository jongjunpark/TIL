for tc in range(1,int(input())+1):
    A, B = map(str,input().split())
    a, b = len(A), len(B)
    count = 0
    i = 0
    while i < a:
        count += 1
        k = i
        if A[i] == B[0]:
            for j in range(b):
                if i < a and A[i] == B[j]:
                    i += 1
                else:
                    i = k+1
                    break
        else:
            i += 1

    print('#{} {}'.format(tc,count))
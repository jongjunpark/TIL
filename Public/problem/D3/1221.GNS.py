num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for x in range(1,T+1):
    t, n = map(str,input().split())
    N = int(n)
    number = list(map(str,input().split()))
    for i in range(len(number)):
        for j in range(len(num)):
            if number[i] == num[j]:
                number[i] = j
    number.sort()
    for i in range(len(number)):
        for j in range(len(num)):
            if number[i] == j:
                number[i] = num[j]
    print(t)
    print(' '.join(number))

def fibo(k):
    a = [0, 1]
    for i in range(2,k+1):
        a.append(a[i-1] + a[i-2])
    return print(a[1:len(a)+1])

input = int(input())
fibo(input)
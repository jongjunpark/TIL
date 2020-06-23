N = int(input())
num = list(map(int,input().split()))
number = int(input())
#약수
factor_sum = 0
multiple_sum = 0
for i in num:
    if number % i == 0:
        factor_sum += i
    if i % number == 0:
        multiple_sum += i
print(factor_sum)
print(multiple_sum)
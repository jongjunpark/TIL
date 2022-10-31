# 배열의 크기 N, 숫자가 더해지는 횟수 M, 연속해서 초과하여 더해질 수 없는 횟수 K
# N(2 <= N <= 1,000), M(1<=M<=10,000), K(1<=K<=10,000)

## 5 8 3 (N, M, K)
## 2 4 5 4 6 (N개의 자연수)

## 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46 

input_a = '5 8 3'
input_b = '2 4 5 4 6'

N, M, K = map(int, input_a.split(' '))
numbers = list(map(int, input_b.split(' ')))
numbers.sort(reverse=True)

# 가장 단순한 방법
# 횟수만큼 반복문 -> M의 갯수가 커지면 문제가 발생할 수 있다.
result = 0

# K를 확인할 카운팅용
cnt = 0

for i in range(M):
    cnt += 1
    if cnt > K:
        cnt = 0
        result += numbers[1]
    else:
        result += numbers[0]
    
print(result, '1번째 solve')

# 규칙을 이용한 수열로 해결
# 큰 수 K번 + 두번째 큰 수 1번이 반복되는 구조

result = 0

# q : 몫, r : 나머지
q, r = divmod(M, K+1)

result = q*(numbers[0]*K + numbers[1]) + r*numbers[0]
print(result, '2번째 solve')

a = int(input())
b = []
for i in range(1, a + 1):
    if a % i == 0:
        print("{0}(은)는 {1}의 약수입니다.".format(i, a))
        b += str(i)

if len(b) == 2:
    print("{0}(은)는 {1}과 {2}로만 나눌 수 있는 소수입니다.".format(a, b[0], b[1]))
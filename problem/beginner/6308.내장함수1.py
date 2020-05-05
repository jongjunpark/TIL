def countdown(a, b):
    remain = 100 - b - 1
    year = 2020 + remain
    return print("%s(은)는 %d년에 100세가 될 것입니다."%(a, year))

input1 = str(input())
input2 = int(input())
countdown(input1, input2)
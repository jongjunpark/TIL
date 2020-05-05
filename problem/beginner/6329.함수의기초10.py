def countdown(k):
    if k > 0:
        k = 11 - k
        return print(k)
    else:
        return print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")

for i in range(0,11):
    countdown(i)
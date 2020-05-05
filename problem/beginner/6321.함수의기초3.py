def test(k):
    if k != 1:
        for i in range(2,k):
            if k % i == 0:
                return False
    else:
        return False

    return True

num = input()
if test(int(num)):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
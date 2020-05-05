name1, name2 = input(), input()
attack1, attack2 = input(), input()
list = ["가위","바위","보"]
if attack1 == list[0]:
    if attack2 == list[0]:
        print("비겼습니다!")
    elif attack2 == list[1]:
        print("{0}가 이겼습니다!".format(attack2))
    else:
        print("{0}가 이겼습니다!".format(attack1))
if attack1 == list[1]:
    if attack2 == list[1]:
        print("비겼습니다!")
    elif attack2 == list[2]:
        print("{0}가 이겼습니다!".format(attack2))
    else:
        print("{0}가 이겼습니다!".format(attack1))
if attack1 == list[2]:
    if attack2 == list[2]:
        print("비겼습니다!")
    elif attack2 == list[1]:
        print("{0}가 이겼습니다!".format(attack1))
    else:
        print("{0}가 이겼습니다!".format(attack2))
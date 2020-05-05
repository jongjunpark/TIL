def check_bracket(data):
    check_list = []

    for i in data:
        if i == '(' or i == '{' or i == '[':
            check_list.append(i)
        elif i == ')':
            if len(check_list) == 0:
                return False
            elif check_list[-1] != '(':
                return False
            else:
                check_list.pop()
        elif i == '}':
            if len(check_list) == 0:
                return False
            elif check_list[-1] != '{':
                return False
            else:
                check_list.pop()
        elif i == ']':
            if len(check_list) == 0:
                return False
            elif check_list[-1] != '[':
                return False
            else:
                check_list.pop()
    if len(check_list) == 0:
        return True
    else:
        return False

T = int(input())
for t in range(1, T+1):
    if check_bracket(input()):
        print("#{} 1".format(t))
    else:
        print("#{} 0".format(t))
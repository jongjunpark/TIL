T = int(input())
for t in range(1,T+1):
    data = list(map(str, input().split()))
    num = []
    for i in data:
        try:
            if '0' <= i <= '9':
                num.append(int(i))

            elif i == '+':
                b = num.pop()
                a = num.pop()
                num.append(a+b)

            elif i == '-':
                b = num.pop()
                a = num.pop()
                num.append(a - b)

            elif i == '*':
                b = num.pop()
                a = num.pop()
                num.append(a * b)

            elif i == '/':
                b = num.pop()
                a = num.pop()
                num.append(a / b)

            else:
                if len(num) > 1:
                    print('#{} error'.format(t))
                    break
                else:
                	print('#{} {}'.format(t, int(num[-1])))

        except:
            print('#{} error'.format(t))
            break
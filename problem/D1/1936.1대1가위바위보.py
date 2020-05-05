inp1, inp2 = map(str, input().split())
if inp1 == '1':
    if inp2 == '2':
        print('A')
    elif inp2 == '3':
        print('B')
elif inp1 == '2':
    if inp2 == '1':
        print('A')
    elif inp2 == '3':
        print('B')
else:
    if inp2 == '1':
        print('B')
    elif inp2 == '2':
        print('A')
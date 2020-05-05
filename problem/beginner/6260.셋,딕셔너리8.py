a = str(input())
b = list(a)

upper = 0
under = 0
ETC = 0
for i in b:
    if ord(i) >= 92:
        under += 1
    elif 90 >= ord(i) >= 65:
        upper += 1
    else:
        ETC += 1

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, under))


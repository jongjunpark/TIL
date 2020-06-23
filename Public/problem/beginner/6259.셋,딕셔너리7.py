a = str(input())
b = list(a)
LETTERS = 0
DIGITS = 0
ETC = 0
for i in b:
    if ord(i) >= 90:
        LETTERS += 1
    elif 60 > ord(i) > 40:
        DIGITS += 1
    else:
        ETC += 1

print("LETTERS {0}\nDIGITS {1}".format(LETTERS, DIGITS))
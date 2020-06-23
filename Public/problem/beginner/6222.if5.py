a = input()
b = ord(a)
if 65 <= b <= 90:
    c = b + 32
    d = chr(c)
    print("%s(ASCII: %d) => %s(ASCII: %d)"%(a,b,d,c))
elif 97 <= b <= 122:
    e = b - 32
    f = chr(e)
    print("%s(ASCII: %d) => %s(ASCII: %d)"%(a,b,f,e))
else:
    print(a)
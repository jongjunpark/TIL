a = ''
for i in range(100,301):
    if (int(i / 100) == 2) and (int(i / 10) % 2 == 0) and (i % 2 == 0):
        a += str(i) + ','
print(a[0:len(a)-1])
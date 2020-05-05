b, c = map(int, input().split(', '))
list1 = []
list2 = []

for i in range(0, b):
    list1 = []
    for j in range(0, c):
        list1.append (i*j)
    list2.append (list1)

print(list2)
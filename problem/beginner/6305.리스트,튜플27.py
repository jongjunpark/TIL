def set1(x):
    return set(x)

list1 = [12,24,35,24,88,120,155,88,120,155]
set1(list1)
list2 = list(set1(list1))

print(sorted(list2))
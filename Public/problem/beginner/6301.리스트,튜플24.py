
list1 = [0, 0, 0, 0]
list2 = [list1 for i in list1[0:3]]
list3 = [list2 for i in list2[0:2]]

print(list3)
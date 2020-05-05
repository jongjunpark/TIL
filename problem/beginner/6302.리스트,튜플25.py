list1 =  [12, 24, 35, 70, 88, 120, 155]
list2 = [val for idx, val in enumerate(list1) if idx == 1 or idx == 2 or idx == 3 or idx == 6]

print(list2)
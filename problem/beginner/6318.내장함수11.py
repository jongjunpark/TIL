str1 = "abcdef"
list_str1 = list(str1)
number = 0, 1, 2, 3, 4, 5
list_num = list(number)
dic = dict(zip(list_str1, list_num))
for key, val in dic.items():
    print("%s: %d"%(key, val))



def find(a, my_list):
    if a in my_list:
        print("%d => True" % a)
    else:
        print("%d => False" % a)


my_list = [2, 4, 6, 8, 10]
print(my_list)
input1 = 5
input2 = 10
find(input1, my_list)
find(input2, my_list)


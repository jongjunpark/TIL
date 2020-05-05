def length(a, b):
    if len(a) > len(b):
        return print(a)
    elif len(b) > len(a):
        return print(b)
    else:
        return

input1, input2 = input().split(', ')
input1 = str(input1)
input2 = str(input2)
length(input1, input2)
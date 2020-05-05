def square(a, b):
    square_a = a * a
    square_b = b * b
    return print("square(%d) => %d\nsquare(%d) => %d" % (a, square_a, b, square_b))


input1, input2 = input().split(',')
input1 = int(input1)
input2 = int(input2)
square(input1, input2)



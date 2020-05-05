
import math

input1, input2, input3, input4 = input().split(', ')
int_1 = int(input1)
int_2 = int(input2)
int_3 = int(input3)
int_4 = int(input4)

def circle(x):
    return 2 * math.pi * x

print("%.2f, %.2f, %.2f, %.2f"%(circle(int_1), circle(int_2), circle(int_3), circle(int_4)))

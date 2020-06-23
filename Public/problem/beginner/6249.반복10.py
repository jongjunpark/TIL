a = list(input())
result_0 = 0; result_1 = 0; result_2 = 0; result_3 = 0; result_4 = 0; result_5 = 0; result_6 = 0; result_7 = 0; result_8 = 0; result_9 = 0
for i in a:
    if i == '0':
        result_0 += 1
    elif i == '1':
        result_1 += 1
    elif i == '2':
        result_2 += 1
    elif i == '3':
        result_3 += 1
    elif i == '4':
        result_4 += 1
    elif i == '5':
        result_5 += 1
    elif i == '6':
        result_6 += 1
    elif i == '7':
        result_7 += 1
    elif i == '8':
        result_8 += 1
    else:
        result_9 += 1
print("0 1 2 3 4 5 6 7 8 9")
print(result_0, result_1, result_2, result_3, result_4, result_5, result_6, result_7, result_8, result_9)
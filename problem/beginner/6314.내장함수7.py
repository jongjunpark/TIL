def filt(num):
    return num % 2 == 0

number = list(range(1,11))
result = filter(filt, number)
print(list(result))

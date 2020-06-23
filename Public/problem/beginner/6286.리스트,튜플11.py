
def num(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return num(n - 1) + num(n - 2)

result = [num(i) for i in range(0,10)]

print(result)

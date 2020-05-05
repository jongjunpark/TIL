N,M = map(int, input().split())
t = int(input())
x = [0,M]
y = [0,N]
for i in range(t):
    idx,tmp = map(int,input().split())
    if idx == 0:
        x.append(tmp)
    else:
        y.append(tmp)
x.sort()
y.sort()
x_length = 0
y_length = 0
for i in range(len(x)-1):
    length = x[i+1] - x[i]
    if length > x_length:
        x_length = length
for i in range(len(y)-1):
    length = y[i+1] - y[i]
    if length > y_length:
        y_length = length
print(x_length * y_length)
W,H = map(int,input().split())
N = int(input())
data = []
for i in range(N):
    tmp = list(map(int, input().split()))
    data.append(tmp)
start = list(map(int, input().split()))
if start[0] == 1:
    start_point = (0,start[1])
elif start[0] == 2:
    start_point = (H,start[1])
elif start[0] == 3:
    start_point = (start[1],0)
else:
    start_point = (start[1],W)
result = 0
for i in range(N):
    if (data[i][0] == 1 and start[0] == 2) or (data[i][0] == 2 and start[0] == 1):
        if data[i][1] + start[1] > (W - data[i][1]) + (W - start[1]):
            result += (W - data[i][1]) + (W - start[1]) + H
        else:
            result += data[i][1] + start[1] + H

    elif (data[i][0] == 3 and start[0] == 4) or (data[i][0] == 4 and start[0] == 3):
        if data[i][1] + start[1] > (H - data[i][1]) + (H - start[1]):
            result += (H - data[i][1]) + (H - start[1]) + W
        else:
            result += data[i][1] + start[1] + W
    elif data[i][0] == 1:
        data_point = (0,data[i][1])
        result += (abs(start_point[0]-data_point[0]) + abs(start_point[1]-data_point[1]))
    elif data[i][0] == 2:
        data_point = (H,data[i][1])
        result += (abs(start_point[0]-data_point[0]) + abs(start_point[1]-data_point[1]))
    elif data[i][0] == 3:
        data_point = (data[i][1],0)
        result += (abs(start_point[0]-data_point[0]) + abs(start_point[1]-data_point[1]))
    else:
        data_point = (data[i][1],W)
        result += (abs(start_point[0] - data_point[0]) + abs(start_point[1] - data_point[1]))
print(result)
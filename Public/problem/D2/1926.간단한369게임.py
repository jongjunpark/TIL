n = int(input())
for i in range(1,n+1):
    if ((i%10 != 0) and (i%10) % 3 == 0)  and ((i//10) != 0 and (i//10) % 3 == 0):
        print('--',end=' ')
    elif ((i%10 != 0) and (i%10) % 3 == 0) or ((i//10) != 0 and (i//10) % 3 == 0):
        print('-',end=' ')
    else:
        print(i,end=' ')
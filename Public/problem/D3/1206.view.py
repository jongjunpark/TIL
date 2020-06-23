for t in range(1,11):
    width = list(map(int,input().split()))
    height = list(map(int,input().split()))
    total = 0
    for n in range(width[0]):
        if height[n] > (height[n-1]) and height[n] > (height[n-2]) and height[n] > (height[n+1]) and height[n] > (height[n+2]):
            first = height[n]
            if height[n-1] >= height[n-2] and height[n-1] >= height[n+1] and height[n-1] >= height[n+2]:
                second = height[n-1]
                total += (first - second)
            elif height[n-2] >= height[n-1] and height[n-2] >= height[n+1] and height[n-2] >= height[n+2]:
                second = height[n-2]
                total += (first - second)
            elif height[n+1] >= height[n-2] and height[n+1] >= height[n-1] and height[n+1] >= height[n+2]:
                second = height[n+1]
                total += (first - second)
            elif height[n+2] >= height[n-2] and height[n+2] >= height[n+1] and height[n+2] >= height[n-1]:
                second = height[n+2]
                total += (first - second)
    print("#{0} {1}".format(t,total))


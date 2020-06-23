count = int(input())
numbers = list(map(int, input().split()))

for j in range(len(numbers)):
    for i in range(1, len(numbers) - j):
        if numbers[i - 1] > numbers[i]:
            numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
print(numbers[int(len(numbers) / 2)])
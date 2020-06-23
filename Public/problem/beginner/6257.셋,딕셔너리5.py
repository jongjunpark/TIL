fruit = ['   apple    ','banana','  melon']

result = {num.strip(): len(num.strip()) for num in fruit}
print(result)
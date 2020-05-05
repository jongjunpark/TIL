#리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
list_a = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
result = [num for num in list_a if num not in 'aeiou']
print("".join(result))
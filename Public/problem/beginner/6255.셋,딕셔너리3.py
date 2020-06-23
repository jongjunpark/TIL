electronic = {"TV": 2000000, "냉장고": 1500000, "책상": 350000, "노트북": 1200000, "가스레인지": 200000, "세탁기": 1000000}
max_value = 0
max_key = ''
while electronic:
    for key, value in electronic.items():
        if value >= max_value:
            max_value = value
            max_key = key
    print('{}: {}'.format(max_key, max_value))
    max_value = 0
    del electronic[max_key]




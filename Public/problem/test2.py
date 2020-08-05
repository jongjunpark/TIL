kim = [100, 300, 10, 0, 40, 0, 0, 70, 65]
lee = [40, 300, 20, 10, 10, 20, 100, 10, 0]
bank = 0
for i in range(len(kim)):
	if bank + kim[i] - lee[i] >= 0:
		print(bank + kim[i] - lee[i])
        bank = 0
	else:
		bank += (kim[i] - lee[i])
		print(0)
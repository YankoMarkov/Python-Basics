hour = int(input())
minute = int(input())

if minute + 15 > 59:
	if hour == 23:
		hour = 0
	else:
		hour += 1
	minute = abs((minute + 15) - 60)
else:
	minute = minute + 15

if minute < 10:
	print(f'{hour}:0{minute}')
else:
	print(f'{hour}:{minute}')

num = int(input())

for number in range(1111, 10000):
	str_num = str(number)
	count = 0
	for digit in range(len(str_num)):
		if int(str_num[digit]) > 0 and num % int(str_num[digit]) == 0:
			count += 1
	if count == 4:
		print(str(number) + ' ', end='')

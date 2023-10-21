first_num = int(input())
second_num = int(input())

for num in range(first_num, second_num + 1):
	num_str = str(num)
	odd = 0
	even = 0
	for n in range(1, len(num_str) + 1):
		if n % 2 == 0:
			even += int(num_str[n - 1])
		else:
			odd += int(num_str[n - 1])
	if even == odd:
		print(str(num) + ' ', end='')

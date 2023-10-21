upper_limit_first_number = int(input())
upper_limit_second_number = int(input())
upper_limit_third_number = int(input())

for num_1 in range(2, upper_limit_first_number + 1):
	for num_2 in range(2, upper_limit_second_number + 1):
		for num_3 in range(2, upper_limit_third_number + 1):
			if num_1 % 2 == 0 and all(num_2 % i for i in range(2, num_2)) and num_3 % 2 == 0:
				print(f'{num_1} {num_2} {num_3}')

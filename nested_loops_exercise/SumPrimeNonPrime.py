command = input()

prime_num = 0
non_prime_num = 0

while command != 'stop':
	num = int(command)
	if num < 0:
		print('Number is negative.')
		command = input()
		continue
	count = 0
	for i in range(1, num + 1):
		if (num / i) % 1 == 0:
			count += 1
	if count == 2:
		prime_num += num
	else:
		non_prime_num += num
	command = input()

print(f'Sum of all prime numbers is: {prime_num}')
print(f'Sum of all non prime numbers is: {non_prime_num}')

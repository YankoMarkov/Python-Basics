count = int(input())

sum_even = 0
sum_odd = 0

for i in range(0, count):
	num = int(input())
	if i % 2 == 0:
		sum_even += num
	else:
		sum_odd += num

if sum_even == sum_odd:
	print('Yes')
	print(f'Sum = {sum_even}')
else:
	print('No')
	diff = abs(sum_even - sum_odd)
	print(f'Diff = {diff}')

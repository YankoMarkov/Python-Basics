import sys

count = int(input())

max_num = -sys.maxsize
sum_num = 0

for i in range(0, count):
	num = int(input())
	if num > max_num:
		max_num = num
	sum_num += num

sum_num -= max_num

if sum_num == max_num:
	print('Yes')
	print(f'Sum = {sum_num}')
else:
	print('No')
	diff = abs(max_num - sum_num)
	print(f'Diff = {diff}')

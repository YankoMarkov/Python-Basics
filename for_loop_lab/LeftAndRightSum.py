count = int(input())

left_sum = 0
right_sum = 0

for i in range(0, count):
	num = int(input())
	left_sum += num

for i in range(0, count):
	num = int(input())
	right_sum += num

if left_sum == right_sum:
	print(f'Yes, sum = {left_sum}')
else:
	diff = abs(left_sum - right_sum)
	print(f'No, diff = {diff}')

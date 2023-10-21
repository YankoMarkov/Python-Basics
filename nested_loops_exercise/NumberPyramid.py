num = int(input())
current = 1
is_current_bigger_then_num = False

for row in range(1, num + 1):
	for col in range(1, row + 1):
		if current > num:
			is_current_bigger_then_num = True
			break
		print(str(current) + ' ', end='')
		current += 1
	if is_current_bigger_then_num:
		break
	print()

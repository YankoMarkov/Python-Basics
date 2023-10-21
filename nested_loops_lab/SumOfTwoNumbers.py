firs_row = int(input())
second_row = int(input())
magic_num = int(input())
count = 0
is_found = False

for i in range(firs_row, second_row + 1):
	for j in range(firs_row, second_row + 1):
		result = i + j
		count += 1
		if result == magic_num:
			print(f'Combination N:{count} ({i} + {j} = {magic_num})')
			is_found = True
			break
	if is_found:
		break

if not is_found:
	print(f'{count} combinations - neither equals {magic_num}')

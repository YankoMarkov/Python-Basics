destination = input()

while destination != 'End':
	min_budget = float(input())
	while True:
		spend_sum = float(input())
		min_budget -= spend_sum
		if min_budget <= 0:
			print(f'Going to {destination}!')
			break
	destination = input()

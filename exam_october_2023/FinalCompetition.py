number_of_dancers = int(input())
number_of_points = float(input())
season = input()
place = input()

total_sum = 0
result = 0

if place == 'Bulgaria':
	total_sum = number_of_points * number_of_dancers
	if season == 'summer':
		result = total_sum - (total_sum * 0.05)
	elif season == 'winter':
		result = total_sum - (total_sum * 0.08)
elif place == 'Abroad':
	total_sum = number_of_points * number_of_dancers
	total_sum = total_sum + (total_sum * 0.5)
	if season == 'summer':
		result = total_sum - (total_sum * 0.10)
	elif season == 'winter':
		result = total_sum - (total_sum * 0.15)

charity = result * 0.75
money_per_dancer = (result - charity) / number_of_dancers

print(f'Charity - {charity:.2f}')
print(f'Money per dancer - {money_per_dancer:.2f}')

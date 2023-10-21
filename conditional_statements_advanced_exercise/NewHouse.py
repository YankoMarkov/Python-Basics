flower = input()
flower_number = int(input())
budget = int(input())
price = 0

if flower == 'Roses':
	if flower_number > 80:
		price = 5 - (5 * 0.1)
	else:
		price = 5
elif flower == 'Dahlias':
	if flower_number > 90:
		price = 3.80 - (3.80 * 0.15)
	else:
		price = 3.80
elif flower == 'Tulips':
	if flower_number > 80:
		price = 2.80 - (2.80 * 0.15)
	else:
		price = 2.80
elif flower == 'Narcissus':
	if flower_number < 120:
		price = 3 + (3 * 0.15)
	else:
		price = 3
elif flower == 'Gladiolus':
	if flower_number < 80:
		price = 2.50 + (2.50 * 0.2)
	else:
		price = 2.50

if budget >= flower_number * price:
	left_sum = budget - flower_number * price
	print(f'Hey, you have a great garden with {flower_number} {flower} and {left_sum:.2f} leva left.')
else:
	need_sum = flower_number * price - budget
	print(f'Not enough money, you need {need_sum:.2f} leva more.')

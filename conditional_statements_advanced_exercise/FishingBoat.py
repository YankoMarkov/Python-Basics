budget = int(input())
season = input()
fisherman_number = int(input())

price = 0.0

if season == 'Spring':
	if fisherman_number <= 6:
		price = 3000 - (3000 * 0.1)
	elif 7 <= fisherman_number <= 11:
		price = 3000 - (3000 * 0.15)
	else:
		price = 3000 - (3000 * 0.25)
	if fisherman_number % 2 == 0:
		price -= (price * 0.05)
elif season == 'Summer' or season == 'Autumn':
	if fisherman_number <= 6:
		price = 4200 - (4200 * 0.1)
	elif 7 <= fisherman_number <= 11:
		price = 4200 - (4200 * 0.15)
	else:
		price = 4200 - (4200 * 0.25)
	if fisherman_number % 2 == 0 and season == 'Summer':
		price -= (price * 0.05)
elif season == 'Winter':
	if fisherman_number <= 6:
		price = 2600 - (2600 * 0.1)
	elif 7 <= fisherman_number <= 11:
		price = 2600 - (2600 * 0.15)
	else:
		price = 2600 - (2600 * 0.25)
	if fisherman_number % 2 == 0:
		price -= (price * 0.05)

if budget >= price:
	left_money = budget - price
	print(f'Yes! You have {left_money:.2f} leva left.')
else:
	needed_money = price - budget
	print(f'Not enough money! You need {needed_money:.2f} leva.')

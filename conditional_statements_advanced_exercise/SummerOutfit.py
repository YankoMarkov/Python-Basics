degree = int(input())
time_of_day = input()

outfit = ''
shoes = ''

if 10 <= degree <= 18:
	if time_of_day == 'Morning':
		outfit = 'Sweatshirt'
		shoes = 'Sneakers'
	elif time_of_day == 'Afternoon':
		outfit = 'Shirt'
		shoes = 'Moccasins'
	elif time_of_day == 'Evening':
		outfit = 'Shirt'
		shoes = 'Moccasins'
elif 18 < degree <= 24:
	if time_of_day == 'Morning':
		outfit = 'Shirt'
		shoes = 'Moccasins'
	elif time_of_day == 'Afternoon':
		outfit = 'T-Shirt'
		shoes = 'Sandals'
	elif time_of_day == 'Evening':
		outfit = 'Shirt'
		shoes = 'Moccasins'
else:
	if time_of_day == 'Morning':
		outfit = 'T-Shirt'
		shoes = 'Sandals'
	elif time_of_day == 'Afternoon':
		outfit = 'Swim Suit'
		shoes = 'Barefoot'
	elif time_of_day == 'Evening':
		outfit = 'Shirt'
		shoes = 'Moccasins'

print(f"It's {degree} degrees, get your {outfit} and {shoes}.")

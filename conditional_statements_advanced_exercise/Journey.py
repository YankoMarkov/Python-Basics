budget = float(input())
season = input()

destination = ''
holiday = ''
price = 0.0

if season == 'summer':
	if budget <= 100:
		price = budget * 0.3
		destination = 'Bulgaria'
		holiday = 'Camp'
	elif 100 < budget <= 1000:
		price = budget * 0.4
		destination = 'Balkans'
		holiday = 'Camp'
	else:
		price = budget * 0.9
		destination = 'Europe'
		holiday = 'Hotel'
elif season == 'winter':
	if budget <= 100:
		price = budget * 0.7
		destination = 'Bulgaria'
	elif 100 < budget <= 1000:
		price = budget * 0.8
		destination = 'Balkans'
	else:
		price = budget * 0.9
		destination = 'Europe'
	holiday = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{holiday} - {price:.2f}')

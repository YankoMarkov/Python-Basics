fruit = input()
day_of_week = input()
quantity = float(input())

price = 0

if day_of_week == 'Saturday' or day_of_week == 'Sunday':
	if fruit == 'banana':
		price = 2.7
	elif fruit == 'apple':
		price = 1.25
	elif fruit == 'orange':
		price = 0.9
	elif fruit == 'grapefruit':
		price = 1.6
	elif fruit == 'kiwi':
		price = 3.0
	elif fruit == 'pineapple':
		price = 5.6
	elif fruit == 'grapes':
		price = 4.2
elif day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
	if fruit == 'banana':
		price = 2.5
	elif fruit == 'apple':
		price = 1.2
	elif fruit == 'orange':
		price = 0.85
	elif fruit == 'grapefruit':
		price = 1.45
	elif fruit == 'kiwi':
		price = 2.7
	elif fruit == 'pineapple':
		price = 5.5
	elif fruit == 'grapes':
		price = 3.85

if price > 0:
	print(f'{quantity * price:.2f}')
else:
	print('error')

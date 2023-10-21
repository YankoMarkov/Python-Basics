city = input()
sells = float(input())

percent = 0.0

if (city != 'Sofia' and city != 'Varna' and city != 'Plovdiv') or sells < 0:
	print('error')
else:
	if 0 <= sells <= 500:
		if city == 'Sofia':
			percent = 5
		elif city == 'Varna':
			percent = 4.5
		elif city == 'Plovdiv':
			percent = 5.5
	elif 500 < sells <= 1000:
		if city == 'Sofia':
			percent = 7
		elif city == 'Varna':
			percent = 7.5
		elif city == 'Plovdiv':
			percent = 8
	elif 1000 < sells <= 10000:
		if city == 'Sofia':
			percent = 8
		elif city == 'Varna':
			percent = 10
		elif city == 'Plovdiv':
			percent = 12
	else:
		if city == 'Sofia':
			percent = 12
		elif city == 'Varna':
			percent = 13
		elif city == 'Plovdiv':
			percent = 14.5
	
	print(f'{sells * (percent / 100):.2f}')

is_sleep = input()
meters = int(input())

days = 1
peak = 8848
meters_climbed = 5364

while True:
	if is_sleep == 'Yes':
		days += 1
	
	if days > 5:
		break
	
	meters_climbed += meters
	
	if meters_climbed >= peak:
		break
	
	is_sleep = input()
	
	if is_sleep == 'END':
		break
	
	meters = int(input())

if meters_climbed >= peak:
	print(f'Goal reached for {days} days!')
else:
	print('Failed!')
	print(f'{meters_climbed}')

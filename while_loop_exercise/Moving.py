width = int(input())
length = int(input())
height = int(input())

apartment_value = width * length * height
free_space = 0

while apartment_value > 0:
	command = input()
	if command == 'Done':
		if apartment_value > 0:
			print(f'{apartment_value} Cubic meters left.')
		else:
			print(f'No more free space! You need {abs(apartment_value)} Cubic meters more.')
		break
	cartons = int(command)
	apartment_value -= cartons
else:
	print(f'No more free space! You need {abs(apartment_value)} Cubic meters more.')

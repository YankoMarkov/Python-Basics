projection_type = input()
rows = int(input())
columns = int(input())

seats = rows * columns

if projection_type == 'Premiere':
	print(f'{seats * 12.0:.2f} leva')
elif projection_type == 'Normal':
	print(f'{seats * 7.5:.2f} leva')
elif projection_type == 'Discount':
	print(f'{seats * 5.0:.2f} leva')

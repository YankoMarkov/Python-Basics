floors = int(input())
rooms = int(input())
result = ''

for floor in range(floors, 0, -1):
	for room in range(0, rooms):
		if floor == floors:
			result += f'L{floor}{room} '
		elif floor % 2 == 0:
			result += f'O{floor}{room} '
		else:
			result += f'A{floor}{room} '
	print(result)
	result = ''

width = int(input())
length = int(input())

pieces = width * length

while pieces > 0:
	command = input()
	if command == 'STOP':
		print(f'{pieces} pieces are left.')
		break
	taken_pieces = int(command)
	pieces -= taken_pieces
else:
	print(f'No more cake left! You need {abs(pieces)} pieces more.')

tournament_number = int(input())
start_points = int(input())

win_tournament_count = 0
total_tournament_points = 0

for i in range(tournament_number):
	tournament_stage = input()
	if tournament_stage == 'W':
		start_points += 2000
		total_tournament_points += 2000
		win_tournament_count += 1
	elif tournament_stage == 'F':
		start_points += 1200
		total_tournament_points += 1200
	elif tournament_stage == 'SF':
		start_points += 720
		total_tournament_points += 720

average_total_tournament_points = total_tournament_points // tournament_number
percent_win_tournament = (win_tournament_count / tournament_number) * 100

print(f'Final points: {start_points}')
print(f'Average points: {average_total_tournament_points}')
print(f'{percent_win_tournament:.2f}%')

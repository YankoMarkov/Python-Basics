actor_name = input()
academy_point = float(input())
assessors_number = int(input())

for i in range(assessors_number):
	assessors_name = input()
	assessors_point = float(input())
	academy_point += (len(assessors_name) * assessors_point) / 2
	if academy_point >= 1250.5:
		break

if academy_point >= 1250.5:
	print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_point:.1f}!')
else:
	needed_point = 1250.5 - academy_point
	print(f'Sorry, {actor_name} you need {needed_point:.1f} more!')

unsatisfactory_rating = int(input())
task_name = input()

unsatisfactory_rating_count = 0
total_rating = 0
number_of_problems = 0
last_name = ''

while task_name != 'Enough':
	rating = int(input())
	if rating <= 4:
		unsatisfactory_rating_count += 1
		if unsatisfactory_rating_count == unsatisfactory_rating:
			print(f'You need a break, {unsatisfactory_rating_count} poor grades.')
			break
	number_of_problems += 1
	total_rating += rating
	last_name = task_name
	task_name = input()
else:
	average_rating = total_rating / number_of_problems
	print(f'Average score: {average_rating:.2f}')
	print(f'Number of problems: {number_of_problems}')
	print(f'Last problem: {last_name}')

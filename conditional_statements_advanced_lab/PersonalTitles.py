age = float(input())
gender = input()


def check_gender_and_print(male, female):
	if gender == 'm':
		print(male)
	elif gender == 'f':
		print(female)


if age < 16:
	check_gender_and_print('Master', 'Miss')
else:
	check_gender_and_print('Mr.', 'Ms.')

jury_number = int(input())
presentation_name = input()
final_assessment = 0
count_assessment = 0

while presentation_name != 'Finish':
	current_assessment = 0
	for i in range(jury_number):
		rating = float(input())
		current_assessment += rating
		final_assessment += rating
		count_assessment += 1
	middle_current_assessment = current_assessment / jury_number
	print(f'{presentation_name} - {middle_current_assessment:.2f}.')
	presentation_name = input()

middle_final_assessment = final_assessment / count_assessment
print(f"Student's final assessment is {middle_final_assessment:.2f}.")

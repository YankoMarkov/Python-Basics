student_name = input()
years_counter = 0
failed_years = 0
total_exam_grade = 0

while years_counter < 12:
	exam_grade = float(input())
	
	if exam_grade < 4:
		failed_years += 1
		if failed_years > 1:
			years_counter += 1
			print(f'{student_name} has been excluded at {years_counter} grade')
			break
		continue
	
	total_exam_grade += exam_grade
	years_counter += 1
else:
	middle_exam_grade = total_exam_grade / years_counter
	print(f'{student_name} graduated. Average grade: {middle_exam_grade:.2f}')

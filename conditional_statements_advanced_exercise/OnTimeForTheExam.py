exam_hour = int(input())
exam_minute = int(input())
coming_hour = int(input())
coming_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
coming_time = coming_hour * 60 + coming_minute
minutes_difference = coming_time - exam_time
hour = abs(minutes_difference) // 60
minute = abs(minutes_difference) % 60

student_arrival = 'Late'

if minutes_difference < -30:
	student_arrival = 'Early'
elif minutes_difference <= 0:
	student_arrival = 'On time'

result = ''
if hour > 0:
	result = f'{hour}:{minute:02} hours '
else:
	result = f'{minute} minutes '

if minutes_difference < 0:
	result += 'before the start'
else:
	result += 'after the start'

print(student_arrival)
print(result)

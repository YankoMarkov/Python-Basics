student_count = 0
total_student_count = 0
standard_count = 0
total_standard_count = 0
kid_count = 0
total_kid_count = 0
total_tickets = 0

command = input()

while command != 'Finish':
	tickets = int(input())
	
	for _ in range(tickets):
		ticket_type = input()
		
		if ticket_type == 'End':
			break
		
		if ticket_type == 'student':
			student_count += 1
			total_student_count += 1
			total_tickets += 1
		elif ticket_type == 'standard':
			standard_count += 1
			total_standard_count += 1
			total_tickets += 1
		elif ticket_type == 'kid':
			kid_count += 1
			total_kid_count += 1
			total_tickets += 1
	
	total_count = student_count + standard_count + kid_count
	student_count = 0
	standard_count = 0
	kid_count = 0
	print(f'{command} - {(total_count / tickets) * 100:.2f}% full.')
	
	command = input()

else:
	print(f'Total tickets: {total_tickets}')
	print(f'{(total_student_count / total_tickets) * 100:.2f}% student tickets.')
	print(f'{(total_standard_count / total_tickets) * 100:.2f}% standard tickets.')
	print(f'{(total_kid_count / total_tickets) * 100:.2f}% kids tickets.')

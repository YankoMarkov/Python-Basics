number_1 = int(input())
number_2 = int(input())
operator = input()

if operator == '+' or operator == '-' or operator == '*':
	if operator == '+':
		result = number_1 + number_2
		even_odd = 'even' if result % 2 == 0 else 'odd'
		print(f'{number_1} + {number_2} = {result} - {even_odd}')
	elif operator == '-':
		result = number_1 - number_2
		even_odd = 'even' if result % 2 == 0 else 'odd'
		print(f'{number_1} - {number_2} = {result} - {even_odd}')
	elif operator == '*':
		result = number_1 * number_2
		even_odd = 'even' if result % 2 == 0 else 'odd'
		print(f'{number_1} * {number_2} = {result} - {even_odd}')
elif operator == '/':
	if number_2 == 0:
		print(f'Cannot divide {number_1} by zero')
	else:
		result = number_1 / number_2
		print(f'{number_1} / {number_2} = {result:.2f}')
elif operator == '%':
	if number_2 == 0:
		print(f'Cannot divide {number_1} by zero')
	else:
		result = number_1 % number_2
		print(f'{number_1} % {number_2} = {result}')

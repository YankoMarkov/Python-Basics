staying_day = int(input())
type_of_room = input()
rating = input()

staying_night = staying_day - 1
price = 0.0
discount = 0

if type_of_room == 'room for one person':
	price = 18.0
elif type_of_room == 'apartment':
	price = 25.0
	if staying_day < 10:
		discount = 0.3
	elif 10 <= staying_day <= 15:
		discount = 0.35
	else:
		discount = 0.5
elif type_of_room == 'president apartment':
	price = 35.0
	if staying_day < 10:
		discount = 0.1
	elif 10 <= staying_day <= 15:
		discount = 0.15
	else:
		discount = 0.2

total = staying_night * price

if discount != 0:
	total -= total * discount

if rating == 'positive':
	total += total * 0.25
elif rating == 'negative':
	total -= total * 0.1

print(f'{total:.2f}')

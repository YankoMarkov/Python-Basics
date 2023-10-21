money_for_holiday = float(input())
owned_money = float(input())

days_counter = 0
spending_counter = 0

while owned_money < money_for_holiday and spending_counter < 5:
	action = input()
	action_money = float(input())
	days_counter += 1
	if action == 'save':
		owned_money += action_money
		spending_counter = 0
	elif action == 'spend':
		owned_money -= action_money
		spending_counter += 1
		if owned_money < 0:
			owned_money = 0

if spending_counter == 5:
	print("You can't save the money.")
	print(days_counter)
if owned_money >= money_for_holiday:
	print(f'You saved the money for {days_counter} days.')

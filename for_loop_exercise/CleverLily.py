lili_age = int(input())
washing_machine = float(input())
toy_price = int(input())

count_money = 0
count_toys = 0
money = 0

for i in range(1, lili_age + 1):
	if i % 2 == 0:
		count_money += 1
		money += count_money * 10
	else:
		count_toys += 1

money_saved = money - (count_money * 1)
money_from_toys = count_toys * toy_price
total_money = money_saved + money_from_toys

if total_money >= washing_machine:
	left_money = total_money - washing_machine
	print(f'Yes! {left_money:.2f}')
else:
	needed_money = washing_machine - total_money
	print(f'No! {needed_money:.2f}')

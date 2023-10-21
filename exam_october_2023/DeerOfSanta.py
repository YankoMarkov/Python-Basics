from math import floor, ceil

number_of_days = int(input())
food_in_kilos = int(input())
food_per_day_first_deer = float(input())
food_per_day_second_deer = float(input())
food_per_day_third_deer = float(input())

total_food_first_deer = food_per_day_first_deer * number_of_days
total_food_second_deer = food_per_day_second_deer * number_of_days
total_food_third_deer = food_per_day_third_deer * number_of_days

total_food_for_deers = total_food_first_deer + total_food_second_deer + total_food_third_deer

if total_food_for_deers < food_in_kilos:
	print(f'{floor(food_in_kilos - total_food_for_deers)} kilos of food left.')
else:
	print(f'{ceil(total_food_for_deers - food_in_kilos)} more kilos of food are needed.')

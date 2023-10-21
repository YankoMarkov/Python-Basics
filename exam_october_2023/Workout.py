from math import ceil

number_of_days = int(input())
kilometers = float(input())

increased_kilometers = kilometers
total_kilometers = kilometers

for day in range(number_of_days):
	percentage = int(input())
	increased_kilometers += increased_kilometers * (percentage / 100)
	total_kilometers += increased_kilometers

if total_kilometers > 1000:
	print(f"You've done a great job running {ceil(total_kilometers - 1000)} more kilometers!")
else:
	print(f"Sorry Mrs. Ivanova, you need to run {ceil(1000 - total_kilometers)} more kilometers")

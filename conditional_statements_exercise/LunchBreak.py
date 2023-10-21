from math import ceil

tv_serial_name = input()
episode_length = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
rest_time = break_duration / 4

total_break = lunch_time + rest_time

if break_duration - total_break < episode_length:
	print(f"You don't have enough time to watch {tv_serial_name}, you need {ceil(episode_length - (break_duration - total_break))} more minutes.")
else:
	print(f"You have enough time to watch {tv_serial_name} and left with {ceil((break_duration - total_break) - episode_length)} minutes free time.")

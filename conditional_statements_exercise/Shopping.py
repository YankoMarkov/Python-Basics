budget = float(input())
video_card_num = int(input())
processor_num = int(input())
ram_num = int(input())

video_card = 250
total_video_card_price = video_card_num * video_card

processor = total_video_card_price * 0.35
ram = total_video_card_price * 0.1

total_processor_price = processor_num * processor
total_ram_price = ram_num * ram

total_price = total_video_card_price + total_processor_price + total_ram_price

if video_card_num > processor_num:
	total_price = total_price - (total_price * 0.15)

if budget >= total_price:
	print(f"You have {(budget - total_price):.2f} leva left!")
else:
	print(f"Not enough money! You need {(total_price - budget):.2f} leva more!")

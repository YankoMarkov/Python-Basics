month = input()
overnight_stays = int(input())

studio_price = 0.0
apartment_price = 0.0

if month == 'May' or month == 'October':
	studio_price = 50
	apartment_price = 65
	if 7 < overnight_stays <= 14:
		studio_price -= studio_price * 0.05
	elif overnight_stays > 14:
		studio_price -= studio_price * 0.3
		apartment_price -= apartment_price * 0.1
elif month == 'June' or month == 'September':
	studio_price = 75.20
	apartment_price = 68.70
	if overnight_stays > 14:
		studio_price -= studio_price * 0.2
		apartment_price -= apartment_price * 0.1
elif month == 'July' or month == 'August':
	studio_price = 76
	apartment_price = 77
	if overnight_stays > 14:
		apartment_price -= apartment_price * 0.1

studio_price_total = studio_price * overnight_stays
apartment_price_total = apartment_price * overnight_stays

print(f'Apartment: {apartment_price_total:.2f} lv.')
print(f'Studio: {studio_price_total:.2f} lv.')

puzzle = 2.6
talking_doll = 3
teddy_bear = 4.1
minion = 8.2
truck = 2

trip_price = float(input())
puzzle_number = int(input())
talking_doll_number = int(input())
teddy_bear_number = int(input())
minion_number = int(input())
truck_number = int(input())

total_toys_number = puzzle_number + talking_doll_number + teddy_bear_number + minion_number + truck_number

total_puzzle = puzzle * puzzle_number
total_talking_doll = talking_doll * talking_doll_number
total_teddy_bear = teddy_bear * teddy_bear_number
total_minion = minion * minion_number
total_truck = truck * truck_number

total_price = total_puzzle + total_talking_doll + total_teddy_bear + total_minion + total_truck

total_price = total_price - (total_price * 0.1)
if total_toys_number >= 50:
	total_price = total_price - (total_price * 0.25)

if total_price >= trip_price:
	print(f"Yes! {(total_price - trip_price):.2f} lv left.")
else:
	print(f"Not enough money! {(trip_price - total_price):.2f} lv needed.")
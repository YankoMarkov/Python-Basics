film_budget = float(input())
extras_number = int(input())
extra_clothing_cost = float(input())

decor = film_budget * 0.1
if extras_number > 150:
	extra_clothing_cost = extra_clothing_cost - (extra_clothing_cost * 0.1)

decor_clothing_cost = decor + (extra_clothing_cost * extras_number)
total_budget = film_budget - decor_clothing_cost

if film_budget < decor_clothing_cost:
	print("Not enough money!")
	print(f"Wingard needs {abs(total_budget):.2f} leva more.")
else:
	print("Action!")
	print(f"Wingard starts filming with {total_budget:.2f} leva left.")

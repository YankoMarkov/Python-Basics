chicken_menu = 10.35
fish_menu = 12.4
vegan_menu = 8.15

chicken_menu_number = int(input())
fish_menu_number = int(input())
vegan_menu_number = int(input())

total_chicken_menu = chicken_menu * chicken_menu_number
total_fish_menu = fish_menu * fish_menu_number
total_vegan_menu = vegan_menu * vegan_menu_number
total_for_menues = total_vegan_menu + total_chicken_menu + total_fish_menu
dessert_price = total_for_menues * 0.2

total = dessert_price + total_for_menues + 2.5
print(total)
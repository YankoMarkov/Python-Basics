parallelepiped_width = int(input())
parallelepiped_height = int(input())
parallelepiped_lenght = int(input())
percent = float(input())

tank_volume = parallelepiped_lenght * parallelepiped_width * parallelepiped_height
liters_volume = tank_volume / 1000
needed_liters = liters_volume * (1 - (percent / 100))

print(needed_liters)
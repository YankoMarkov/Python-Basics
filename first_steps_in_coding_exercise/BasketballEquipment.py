annual_fee = int(input())

basketball_shoes = annual_fee - (annual_fee * 0.4)
basketball_team = basketball_shoes - (basketball_shoes * 0.2)
a_basketball = basketball_team / 4
basketball_accessories = a_basketball / 5

total = annual_fee + basketball_shoes + basketball_team + a_basketball + basketball_accessories
print(total)
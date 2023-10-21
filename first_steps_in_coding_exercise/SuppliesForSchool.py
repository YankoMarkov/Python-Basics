pens_pack = 5.8
markers_pack = 7.2
cleaning_per_liter = 1.2

pens_pack_number = int(input())
markers_pack_number = int(input())
cleaning_liters = int(input())
discount = int(input())

total_pens_pack = pens_pack * pens_pack_number
total_markers_pack = markers_pack * markers_pack_number
total_cleaning_liters = cleaning_per_liter * cleaning_liters

total_money = total_pens_pack + total_markers_pack + total_cleaning_liters
result = total_money - (total_money * (discount / 100))

print(result)
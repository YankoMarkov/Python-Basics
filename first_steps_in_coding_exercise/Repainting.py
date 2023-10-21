nylon_per_sq_m = 1.5
paint_per_liter = 14.5
paint_thinner = 5.0
bags = 0.4

nylon_sq_meters = int(input())
paynt_liters = int(input())
paint_thinner_liters = int(input())
worker_hours = int(input())

total_nylon_sq_meters = nylon_per_sq_m * (nylon_sq_meters + 2)
total_paint_liters = paint_per_liter * (paynt_liters + (paynt_liters * 0.1))
total_paint_thinner = paint_thinner * paint_thinner_liters
total_for_mterisls = total_nylon_sq_meters + total_paint_liters + total_paint_thinner + bags
worker_total_sum = (total_for_mterisls * 0.3) * 8

total_sum = total_for_mterisls + worker_total_sum
print(total_sum)
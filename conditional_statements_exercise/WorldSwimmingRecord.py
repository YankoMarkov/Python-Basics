from math import floor

record_in_second = float(input())
distance_in_meters = float(input())
time_in_second_per_meter = float(input())

total_distance_in_seconds = distance_in_meters * time_in_second_per_meter
water_resistance_in_seconds = floor(distance_in_meters / 15) * 12.5
total_time = total_distance_in_seconds + water_resistance_in_seconds

if total_time < record_in_second:
	print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
	print(f"No, he failed! He was {(total_time - record_in_second):.2f} seconds slower.")

pages_numbers = int(input())
pages_per_hour = int(input())
days_number = int(input())

total_time_for_reading = pages_numbers // pages_per_hour
hours_per_day = total_time_for_reading // days_number

print(hours_per_day)
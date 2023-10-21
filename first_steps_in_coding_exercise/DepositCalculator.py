deposit = float(input())
periad_in_months = int(input())
annual_interest = float(input())

sum = deposit + periad_in_months * ((deposit * (annual_interest / 100)) / 12)

print(sum)
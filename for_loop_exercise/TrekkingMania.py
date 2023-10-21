group_number = int(input())

musala_num_people = 0
monblan_num_people = 0
kilimandjaro_num_people = 0
k2_num_people = 0
everest_num_people = 0

for i in range(group_number):
	people_number = int(input())
	if people_number <= 5:
		musala_num_people += people_number
	elif 6 <= people_number <= 12:
		monblan_num_people += people_number
	elif 13 <= people_number <= 25:
		kilimandjaro_num_people += people_number
	elif 26 <= people_number <= 40:
		k2_num_people += people_number
	else:
		everest_num_people += people_number

total_people = musala_num_people + monblan_num_people + kilimandjaro_num_people + k2_num_people + everest_num_people
p1 = musala_num_people / total_people * 100
p2 = monblan_num_people / total_people * 100
p3 = kilimandjaro_num_people / total_people * 100
p4 = k2_num_people / total_people * 100
p5 = everest_num_people / total_people * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')

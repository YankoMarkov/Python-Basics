count = int(input())

sum_p1 = 0
sum_p2 = 0
sum_p3 = 0
sum_p4 = 0
sum_p5 = 0

for i in range(0, count):
	num = int(input())
	if num < 200:
		sum_p1 += 1
	elif 200 <= num < 400:
		sum_p2 += 1
	elif 400 <= num < 600:
		sum_p3 += 1
	elif 600 <= num < 800:
		sum_p4 += 1
	else:
		sum_p5 += 1

p1 = sum_p1 / count * 100
p2 = sum_p2 / count * 100
p3 = sum_p3 / count * 100
p4 = sum_p4 / count * 100
p5 = sum_p5 / count * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')

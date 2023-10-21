text = input().lower()

num = 0

for char in text:
	if char == 'a':
		num += 1
	elif char == 'e':
		num += 2
	elif char == 'i':
		num += 3
	elif char == 'o':
		num += 4
	elif char == 'u':
		num += 5

print(num)

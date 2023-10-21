num = int(input())
count = 0

for i in range(num + 1):
	for j in range(num + 1):
		for k in range(num + 1):
			result = i + j + k
			if result == num:
				count += 1

print(count)

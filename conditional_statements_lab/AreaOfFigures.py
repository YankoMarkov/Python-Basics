from math import pi

shape = input()
square_size = 0.0
rectangle_a = 0.0
rectangle_b = 0.0
circle_radios = 0.0
triangle_length = 0.0
triangle_height = 0.0

if shape == 'square':
	square_size = float(input())
	print(f'{square_size ** 2:.3f}')
elif shape == 'rectangle':
	rectangle_a = float(input())
	rectangle_b = float(input())
	print(f'{rectangle_a * rectangle_b:.3f}')
elif shape == 'circle':
	circle_radios = float(input())
	print(f'{pi * (circle_radios ** 2):.3f}')
else:
	triangle_height = float(input())
	triangle_length = float(input())
	print(f'{(triangle_height * triangle_length) / 2:.3f}')
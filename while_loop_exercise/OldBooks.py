wanted_book = input()
book = input()
book_count = 0

while book != 'No More Books':
	if book == wanted_book:
		print(f'You checked {book_count} books and found it.')
		break
	book = input()
	book_count += 1
else:
	print('The book you search is not here!')
	print(f'You checked {book_count} books.')

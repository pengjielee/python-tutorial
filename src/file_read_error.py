try:
	with open('pi1.txt') as file_object:
		content = file_object.read()
		print(content.rstrip())
except FileNotFoundError:
	print('file does not exist.')
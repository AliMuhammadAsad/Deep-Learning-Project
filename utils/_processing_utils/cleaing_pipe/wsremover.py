def remover(file):
	with open(file, 'r', encoding='utf-8') as f:
		lines = f.readlines()
	
	cleaned_lines = [line.strip() + '\n' for line in lines]
	
	with open(file, 'w', encoding='utf-8') as f:
		f.writelines(cleaned_lines)


if __name__ == '__main__':
	file = input()
	remover(file)
	print("Complete")
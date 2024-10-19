def count_couplet(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines if line.strip()]

    couplets = 0
    for i in range(0, len(lines), 2):
        # if i+1 < len(lines) and lines[i] and lines[i+1]:
        #     couplets += 1

        if i + 1 < len(lines):
            couplets += 1
    
    return couplets

file = input('Enter the file name: ')
# file = input('Enter the file name: ')
print(f'The number of couplets in the file is {count_couplet(file)}')
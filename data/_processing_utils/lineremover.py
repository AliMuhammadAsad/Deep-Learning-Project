def remover(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_content = []
    newline_count = 0

    for line in lines:
        if line.strip() == '':
            newline_count += 1
        else:
            newline_count = 0
        
        if newline_count < 2:
            new_content.append(line)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(new_content)

file = input()
remover(file)
print('Complete')
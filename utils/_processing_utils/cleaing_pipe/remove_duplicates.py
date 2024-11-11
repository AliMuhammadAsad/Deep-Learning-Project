def remover(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    unique_lines = list(dict.fromkeys(lines))

    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(unique_lines)

file = input()
remover(file)
print('Duplicates removed successfully!')
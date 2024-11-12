def count_couplet(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    couplets = len(lines) // 2
    return couplets

if __name__ == '__main__':
    file = input()
    total_couplets = count_couplet(file)
    print(f'The number of couplets in the file is {total_couplets}')

    out = "desc.txt"
    with open(out, 'w', encoding='utf-8') as f:
        f.write(f"Couplets Count: {total_couplets}\n")
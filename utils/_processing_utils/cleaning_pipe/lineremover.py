def remover(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    with open(file, 'w', encoding='utf-8') as f:
        for line in lines:
            if line.strip():
                f.write(line)

if __name__ == '__main__': 
    file = input()
    remover(file)
    print('Complete')
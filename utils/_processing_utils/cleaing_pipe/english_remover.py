import re, os

if __name__ == '__main__':
    infile = input()
    out = infile

    # Read the contents of the text file
    with open(infile, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove all English characters (a-z, A-Z) using regex
    cleaned_text = re.sub(r'[a-zA-Z]', '', text)
    cleaned_text = re.sub(r'[\\/\(\)|\[\]{}]', '', cleaned_text)
    # remove numbers as well
    cleaned_text = re.sub(r'[1234567890]', '', cleaned_text)

    # Write the cleaned text back to a new file
    with open(out, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

    print("English characters removed successfully!")

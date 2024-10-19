import re

file = input()

with open(file, 'r', encoding='utf-8') as f:
    text = f.read()

cleaned_text = re.sub(r'[a-zA-Z]', '', text)
# remove numbers as well
cleaned_text = re.sub(r'[0-9]', '', cleaned_text)
# remove , : and [] and //
cleaned_text = re.sub(r'[,:\[\]/]', '', cleaned_text)

with open(file, 'w', encoding='utf-8') as f:
    f.write(cleaned_text)

print("English text removed!")
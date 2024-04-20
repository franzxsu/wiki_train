
# pattern = re.compile(r"CAPITULO\s+\d+\s+CHAPTER\s+\d+")

import re

# List of replacement words
replacement_words = [
    'GENESIS', 'EXODO', 'LEVITICO', 'NUMEROS', 'DEUTERONOMIO', 'JOSUE',
    'OC-OCOM', 'RUT', '1 SAMUEL', '2 SAMUEL', '1 AR-ARI', '2 AR-ARI', '1 CRONICAS', '2 CRONICAS',
    'ESDRAS', 'NEHEMIAS', 'ESTER', 'JOB', 'DAGITI PROVERBIOS', 'ECLESIASTES',
    'CANTA NI SALOMON', 'ISAIAS', 'JEREMIAS', 'DAGITI UN-UNNOY', 'EZEQUIEL', 'DANIEL', 'OSEAS',
    'JOEL', 'AMOS', 'ABDIAS', 'JONAS', 'MIKIAS', 'NAHUM', 'HABACUC', 'SOFONIAS', 'HAGGEO', 'ZACARIAS', 
    'MALAKIAS'
]

# Read from the file
with open('outputc.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Initialize modified text
modified_text = text

# Iterate over replacement words
for word in replacement_words:
    # Construct pattern with current word
    pattern = re.compile(r"\d+\s+\n\s" + re.escape(word) + r"\s+\d+")
    # Remove the pattern from the text
    modified_text = re.sub(pattern, '', modified_text)

# Write the modified text back to the file
with open('output3.txt', 'w', encoding='utf-8') as file:
    file.write(modified_text)

print("Pattern removed successfully.")

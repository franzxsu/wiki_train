import re


# pattern = re.compile(r"CAPITULO\s+\d+\s+CHAPTER\s+\d+")


pattern = re.compile(r"\s+EPHESIANS\s+\d+\s+")

# Read from the file
with open('output3.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Remove the pattern from the text
modified_text = re.sub(pattern, '', text)

# Write the modified text back to the file
with open('output3.txt', 'w', encoding='utf-8') as file:
    file.write(modified_text)

print("Pattern removed successfully.")
import re

# Define the regex pattern to match numbered sentences
pattern = r'(\d+)\s+(.+?)\s+(\d+)\s+(.+?)(?=\d|$)'

# Open the input file in binary mode and decode with UTF-8
with open('output3.txt', 'rb') as file:
    text = file.read().decode('utf-8', errors='ignore')

# Find all matches using the regex pattern
matches = re.findall(pattern, text, re.DOTALL)

# Open the output file to write extracted parallel sentences
with open('parallel_corpora.txt', 'w', encoding='utf-8') as output_file:
    # Iterate over matches and write parallel sentences into the output file
    for match in matches:
        num1, sent1, num2, sent2 = match
        # Remove multiple spaces and replace them with a single space
        sent1 = re.sub(r'\s+', ' ', sent1.strip())
        sent2 = re.sub(r'\s+', ' ', sent2.strip())
        # Write both sentences with their respective numbers and a separator
        output_file.write(num1 + '\t' + sent1 + ' || ' + sent2 + '\n')
        # Add a newline before a new number
        output_file.write('\n')

# Open the output file again to remove double newlines
with open('parallel_corpora.txt', 'r', encoding='utf-8') as input_file:
    text = input_file.read()

# Remove double newlines and ensure only one newline at the end
text = re.sub(r'\n{2,}', '\n', text.strip()) + '\n'

# Write the modified text back to the output file
with open('parallel_corpora.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(text)

print("Extraction complete. Parallel sentences written to parallel_corpora.txt.")

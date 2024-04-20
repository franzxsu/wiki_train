import re

# Define the regex pattern to match numbered sentences
pattern = r'(\d+)\s+(.+?)\s+(\d+)\s+(.+?)(?=\d|$)'

# Open the input file in binary mode and decode with UTF-8
with open('output2.txt', 'rb') as file:
    text = file.read().decode('utf-8', errors='ignore')

# Find all matches using the regex pattern
matches = re.findall(pattern, text, re.DOTALL)

# Open the output file to write extracted parallel sentences
with open('parallel_corpora.txt', 'w', encoding='utf-8') as output_file:
    # Iterate over matches and write parallel sentences into the output file
    for match in matches:
        num1, sent1, num2, sent2 = match
        # Write both sentences with their respective numbers
        output_file.write(num1 + '\t' + sent1.strip() + '\n')
        output_file.write(num2 + '\t' + sent2.strip() + '\n')

print("Extraction complete. Parallel sentences written to parallel_corpora.txt.")

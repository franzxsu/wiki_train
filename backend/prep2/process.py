# Define the input file path
input_file = "parallel_corpora.txt"

# Define the output file paths for Ilocano and English
ilocano_output_file = "ilocano.txt"
english_output_file = "english.txt"

# Open the input file
with open(input_file, "r", encoding="utf-8") as file:
    # Read the lines from the file
    lines = file.readlines()

# Open the output files for writing
with open(ilocano_output_file, "w", encoding="utf-8") as ilocano_file, \
     open(english_output_file, "w", encoding="utf-8") as english_file:
    # Iterate over the lines
    for line in lines:
        # Split the line by "||" to separate Ilocano and English verses
        parts = line.split("||")

        # Extract the Ilocano and English verses
        ilocano_verse = parts[0].strip()
        english_verse = parts[1].strip()

        # Write the Ilocano and English verses to their respective files
        ilocano_file.write(ilocano_verse + "\n")
        english_file.write(english_verse + "\n")

print("Separation into Ilocano and English files completed.")

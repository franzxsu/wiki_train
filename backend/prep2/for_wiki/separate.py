import csv

def extract_sentences(input_file, output_file):
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        sentences = []
        for row in reader:
            sentence = row['First Paragraph']
            start_index = sentence.find("<START>")
            end_index = sentence.find("<END>")
            if start_index != -1 and end_index != -1:
                sentence = sentence[start_index + len("<START>"):end_index].strip()
                sentences.append(sentence)

    with open(output_file, 'w', encoding='utf-8') as txtfile:
        txtfile.write('\n'.join(sentences))

    print(f"Sentences extracted and saved to {output_file} successfully.")

ilokano_csv_file = 'ilokano.csv'
english_csv_file = 'english.csv'

ilokano_output_file = 'ilokano.txt'
english_output_file = 'english.txt'

extract_sentences(ilokano_csv_file, ilokano_output_file)
extract_sentences(english_csv_file, english_output_file)

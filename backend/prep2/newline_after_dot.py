def insert_newline_after_dot(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert newline after each dot
    content_with_newlines = content.replace('.', '.\n')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content_with_newlines)

ilocano_input_file = 'ilocano.txt'
ilocano_output_file = 'ilocano2.txt'

english_input_file = 'english.txt'
english_output_file = 'english2.txt'

insert_newline_after_dot(ilocano_input_file, ilocano_output_file)
insert_newline_after_dot(english_input_file, english_output_file)

print("Newlines inserted after dots in both files.")

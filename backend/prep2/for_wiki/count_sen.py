def count_sentences_in_line(text):
    return len(text.split('.'))

def find_lines_with_different_sentence_counts(ilocano_file, english_file):
    ilocano_lines_to_keep = []
    english_lines_to_keep = []

    with open(ilocano_file, 'r', encoding='utf-8') as ilocano_f, \
         open(english_file, 'r', encoding='utf-8') as english_f:
        ilocano_lines = ilocano_f.readlines()
        english_lines = english_f.readlines()

    for ilocano_line, english_line in zip(ilocano_lines, english_lines):
        ilocano_sentence_count = count_sentences_in_line(ilocano_line)
        english_sentence_count = count_sentences_in_line(english_line)
        if ilocano_sentence_count == english_sentence_count:
            ilocano_lines_to_keep.append(ilocano_line)
            english_lines_to_keep.append(english_line)

    ilocano_output_file = 'ilokano_new.txt'
    english_output_file = 'english_new.txt'

    with open(ilocano_output_file, 'w', encoding='utf-8') as ilocano_f:
        ilocano_f.writelines(ilocano_lines_to_keep)

    with open(english_output_file, 'w', encoding='utf-8') as english_f:
        english_f.writelines(english_lines_to_keep)

    print("Retained lines saved to separate files.")

ilocano_file = 'ilokano.txt'
english_file = 'english.txt'

find_lines_with_different_sentence_counts(ilocano_file, english_file)

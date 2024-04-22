def count_dots(sentence):
    return sentence.count(',')

def filter_sentences(ilocano_sentences, english_sentences):
    filtered_ilocano = []
    filtered_english = []
    for ilocano_sentence, english_sentence in zip(ilocano_sentences, english_sentences):
        ilocano_dot_count = count_dots(ilocano_sentence)
        english_dot_count = count_dots(english_sentence)
        if ilocano_dot_count == english_dot_count:
            filtered_ilocano.append(ilocano_sentence.strip())
            filtered_english.append(english_sentence.strip())
    return filtered_ilocano, filtered_english

ilocano_file = 'filtered_ilocano.txt'
english_file = 'filtered_english.txt'
filtered_ilocano_file = 'ilo.txt'
filtered_english_file = 'en.txt'

with open(ilocano_file, 'r', encoding='utf-8') as ilocano_f, \
     open(english_file, 'r', encoding='utf-8') as english_f:
    ilocano_sentences = ilocano_f.readlines()
    english_sentences = english_f.readlines()

filtered_ilocano, filtered_english = filter_sentences(ilocano_sentences, english_sentences)

with open(filtered_ilocano_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(filtered_ilocano))

with open(filtered_english_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(filtered_english))

print("Filtered sentences written to new files.")

def count_words(sentence):
    # Split the sentence by whitespace and count the words
    return len(sentence.split())

def compare_word_counts(ilocano_sentences, english_sentences, threshold=100):
    for ilocano_sentence, english_sentence in zip(ilocano_sentences, english_sentences):
        ilocano_word_count = count_words(ilocano_sentence)
        english_word_count = count_words(english_sentence)
        if abs(ilocano_word_count - english_word_count) >= threshold:
            print("Ilocano Sentence:", ilocano_sentence.strip())
            print("English Sentence:", english_sentence.strip())
            print(abs(ilocano_word_count - english_word_count))
            print()

ilocano_file = 'filtered_ilocano.txt'
english_file = 'filtered_english.txt'

with open(ilocano_file, 'r', encoding='utf-8') as ilocano_f, \
     open(english_file, 'r', encoding='utf-8') as english_f:
    ilocano_sentences = ilocano_f.readlines()
    english_sentences = english_f.readlines()

compare_word_counts(ilocano_sentences, english_sentences, threshold=20)

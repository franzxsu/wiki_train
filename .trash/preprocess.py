import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

ilokano_data = pd.read_csv("ilokano.csv")
english_data = pd.read_csv("english.csv")

ilokano_data["text"] = ilokano_data["Title"] + " " + ilokano_data["First Paragraph"]
english_data["text"] = english_data["Title"] + " " + english_data["First Paragraph"]

tokenizer_ilo = Tokenizer(num_words=5000)  # Change num_words as needed
tokenizer_eng = Tokenizer(num_words=5000)

tokenizer_ilo.fit_on_texts(ilokano_data["text"])
tokenizer_eng.fit_on_texts(english_data["text"])

ilokano_sequences = tokenizer_ilo.texts_to_sequences(ilokano_data["text"])
english_sequences = tokenizer_eng.texts_to_sequences(english_data["text"])

max_length = max(len(seq) for seq in ilokano_sequences)
ilokano_padded = pad_sequences(ilokano_sequences, maxlen=max_length, padding='post')
english_padded = pad_sequences(english_sequences, maxlen=max_length, padding='post')

model = Sequential()
model.add(Embedding(5000, 128, input_length=max_length))  # Adjust embedding dimensions
model.add(LSTM(256))  # Adjust LSTM units
model.add(Dense(5000, activation='softmax'))  # Adjust output layer size for English vocab

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(ilokano_padded, english_padded, epochs=10)  # Adjust epochs for training time

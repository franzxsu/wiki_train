import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense, Embedding

# Read CSV files
english_data = pd.read_csv("backend/english.csv")
ilokano_data = pd.read_csv("backend/ilokano.csv")

# Prepare data
english_texts = english_data["English"].values
ilokano_texts = ilokano_data["Ilokano"].values

# Tokenize text
tokenizer_eng = Tokenizer()
tokenizer_eng.fit_on_texts(english_texts)
eng_sequences = tokenizer_eng.texts_to_sequences(english_texts)

tokenizer_ilo = Tokenizer()
tokenizer_ilo.fit_on_texts(ilokano_texts)
ilo_sequences = tokenizer_ilo.texts_to_sequences(ilokano_texts)

# Pad sequences
eng_sequences_padded = pad_sequences(eng_sequences, padding='post')
ilo_sequences_padded = pad_sequences(ilo_sequences, padding='post')

# Define model
input_eng = Input(shape=(None,))
emb_eng = Embedding(input_dim=len(tokenizer_eng.word_index)+1, output_dim=256)(input_eng)
encoder = LSTM(256, return_state=True)
_, state_h, state_c = encoder(emb_eng)
encoder_states = [state_h, state_c]

input_ilo = Input(shape=(None,))
emb_ilo = Embedding(input_dim=len(tokenizer_ilo.word_index)+1, output_dim=256)(input_ilo)
decoder = LSTM(256, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder(emb_ilo, initial_state=encoder_states)
decoder_dense = Dense(len(tokenizer_ilo.word_index)+1, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

model = Model([input_eng, input_ilo], decoder_outputs)

# Compile model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train model
model.fit([eng_sequences_padded, ilo_sequences_padded[:, :-1]], ilo_sequences_padded[:, 1:],
          batch_size=64,
          epochs=50,
          validation_split=0.2)

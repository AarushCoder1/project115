import tensorflow.keras
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentence = ["Awesome Camera. Worth the price"]

# Tokenization
tokenizer = Tokenizer(num_words = 10000, oov_token = '<OOV>')
tokenizer.fit_on_texts(sentence)
# Create a word_index dictionary
word_index = tokenizer.word_index
sequence = tokenizer.texts_to_sequences(sentence)

# Padding the sequence
padded = pad_sequences(sequence, maxlen = 100, padding = 'post', truncating='post')
# Define the model using .h5 file
model = tensorflow.keras.models.load_model('Text_emotion.h5')
# Test the model
result = model.predict(padded)

# Print the result
predict_class = np.argmax(result, axis = 1)
print(predict_class)

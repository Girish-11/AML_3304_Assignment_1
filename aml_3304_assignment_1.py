# -*- coding: utf-8 -*-
"""AML_3304_Assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yrKyRXraHOoJhkrSFkNzSV5t_M-3uhfY
"""

import nltk
import random
from nltk.util import ngrams
from collections import defaultdict, Counter

sample_text = """
Once upon a time, in a land far, far away, there lived a king and queen who had a beautiful daughter. The princess was kind and gentle, and everyone loved her.
"""

nltk.download('punkt')
tokens = nltk.word_tokenize(sample_text.lower())
print(tokens)

bigrams = list(ngrams(tokens, 2))
bigram_freq = defaultdict(Counter)

for w1, w2 in bigrams:
    bigram_freq[w1][w2] += 1

print(bigram_freq)

def generate_text(seed, n_words):
    result = [seed]
    for _ in range(n_words):
        next_word_options = bigram_freq[result[-1]]
        next_word = random.choices(list(next_word_options.keys()), list(next_word_options.values()))[0]
        result.append(next_word)
    return ' '.join(result)

generated_text = generate_text('princess', 5)
print(generated_text)

import nltk
import random
from nltk import word_tokenize, sent_tokenize
from nltk.lm import MLE
from nltk.lm.preprocessing import padded_everygram_pipeline

old_text = "your_previous_text_data"
new_text = "your_new_text_data"
combined_text = old_text + " " + new_text

sent_tokens = sent_tokenize(combined_text)
word_tokens = [word_tokenize(t) for t in sent_tokens]

n = 3
train_data, padded_sents = padded_everygram_pipeline(n, word_tokens)

model = MLE(n)
model.fit(train_data, padded_sents)

def generate_text(prompt, num_words, model):
    word_list = model.generate(num_words, text_seed=prompt.split())
    response = ' '.join(word_list)
    return response

# Example questions
questions = [
    "What is the importance",
    "How does it work",
    "What are the benefits",
    "How can I improve",
    "What should I consider"
]

for question in questions:
    print(f"Question: {question}")
    print(f"Answer: {generate_text(question, 20, model)}")
    print("\n")

import nltk
from nltk import bigrams, FreqDist
from nltk.util import ngrams
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
from random import choice

text = "Natural language processing is a subfield of linguistics, computer science, and artificial intelligence \
concerned with the interactions between computers and human language. In particular, it focuses on programming \
computers to process and analyze large amounts of natural language data."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Generate bigrams and their frequency distribution
bigrams = list(ngrams(tokens, 2))
bigram_freq_dist = FreqDist(bigrams)

# Prepare the dataset for training
train_data, padded_sents = padded_everygram_pipeline(2, tokens)

# Train the bigram model
model = MLE(2)
model.fit(train_data, padded_sents)

def generate_sentence(model, num_words, seed_word):
    sentence = [seed_word]
    for _ in range(num_words - 1):
        next_word = model.generate(1, text_seed=sentence)
        sentence.append(next_word)

    return ' '.join(sentence)

# Example questions to the model
questions = [
    "What is natural language processing?",
    "How does artificial intelligence relate to linguistics?",
    "Can computers understand human language?",
]

# Generate answers for the questions
for question in questions:
    tokens = nltk.word_tokenize(question)
    seed_word = choice(tokens)
    generated_sentence = generate_sentence(model, 10, seed_word)
    print(f"Q: {question}\nA: {generated_sentence}\n")


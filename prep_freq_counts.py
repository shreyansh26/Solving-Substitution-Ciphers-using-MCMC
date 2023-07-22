from nltk.corpus import gutenberg
import string
import pickle
from collections import defaultdict

chars_to_remove = list(string.punctuation) + list(map(str, range(0,10)))

# Collect stories to form a corpus of large "typcial" English text
story_words = gutenberg.words('austen-emma.txt') + gutenberg.words('austen-persuasion.txt') + gutenberg.words('austen-sense.txt')

words_list = []

# Cleaning
for word in story_words:
	if len(word) <= 1:
		continue
	if any(c in chars_to_remove for c in word):
		continue
	words_list.append(word.lower())

text = " ".join(words_list)

def dd():
	return 0

freq_counts = defaultdict(dd)

# Add counts to dictionary where keys are tuples of characters (bigrams)
for idx in range(len(text)-1):
	freq_counts[(text[idx], text[idx+1])] += 1

print(freq_counts)

# Save frequency counts
with open('freq_counts.pkl', 'wb') as f:
    pickle.dump(freq_counts, f)
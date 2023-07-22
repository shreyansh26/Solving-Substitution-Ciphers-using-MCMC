import pickle
import random
import math

alphabets = "abcdefghijklmnopqrstuvwxyz"
assert len(alphabets) == 26

def dd():
	return 0

with open('freq_counts.pkl', 'rb') as f:
	freq_counts = pickle.load(f)

def score(text):
	val = 0
	for idx in range(len(text)-1):
		s = freq_counts.get((text[idx], text[idx+1]), 0)
		# Using log helps avoid underflow/overflow issues due to long multiplication chains, as now we can simply add log values
		# Add 1 to prevent underflow when s = 0
		val += math.log(s + 1)
	return val

# Apply mapping to text for decryption
def decrypt(text, mapping):
	new_text = ''

	for i in text:
		if i == ' ':
			new_text += ' '
		else:
			new_text += mapping[i] 

	return new_text

def solve(text, plain_text, curr_mapping, curr_score):
	for idx in range(25000):
		a1, a2 = random.sample(alphabets, 2)
		new_mapping = curr_mapping.copy()
		new_mapping[a1] = curr_mapping[a2]
		new_mapping[a2] = curr_mapping[a1]

		new_score = score(decrypt(text, new_mapping))

		# Acceptance testing
		# Accept
		if new_score > curr_score:
			curr_score = new_score
			curr_mapping = new_mapping
		# Accept
		elif (new_score - curr_score) > math.log(random.uniform(0, 1)):
			curr_score = new_score
			curr_mapping = new_mapping
		# Reject
		else:
			pass

		if idx % 100 == 0:
			decrypted_text = decrypt(text, curr_mapping)
			print(idx)
			print(decrypted_text)
			if decrypted_text == plain_text:
				break


if __name__ == "__main__":
	cipher_text = open('ciphertext.txt', 'r').read()
	plain_text = open('plaintext.txt', 'r').read()


	curr_mapping = {k: k for k in alphabets}
	curr_score = score(decrypt(cipher_text, curr_mapping))

	solve(cipher_text, plain_text, curr_mapping, curr_score)
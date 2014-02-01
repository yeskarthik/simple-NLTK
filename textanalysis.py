# Simple use of NLTK to get rid of articles/non useful words in a sentence

from collections import OrderedDict
import nltk
from nltk.tag.simplify import simplify_wsj_tag

arnab = []
rahul = []

with open('rginterview.txt','r') as f:
	for line in f:
		if line[0] == 'A':
			arnab.append(line[6:].lower())
		else:
			rahul.append(line[6:].lower())

noneed = ['CNJ', 'DET', 'PRO', 'P', 'TO', 'WH', 'V', 'VD', 'VG', 'VN', '.', ',', '?']

def getFreqDistOfUsefulWords(sentences):
	wordFreq = {}
	
	for sent in sentences:
		sanitized_sent = ''.join(e for e in sent if e.isalnum() or e == ' ')
		tokens = nltk.word_tokenize(sanitized_sent)
		tagged_tokens = nltk.pos_tag(tokens)
		simplified = [(word, simplify_wsj_tag(tag)) for word, tag in tagged_tokens]
		words_req = [key for key, val in simplified if val not in noneed]

		for word in words_req:
			if word in wordFreq:
				wordFreq[word] += 1
			else:
				wordFreq[word] = 1

	wordFreqOD = OrderedDict(sorted(wordFreq.items(), key=lambda t: t[1], reverse=True))

	for key, value in wordFreqOD.items():
		print key + " : " + str(value)

	return wordFreqOD

getFreqDistOfUsefulWords(rahul)
getFreqDistOfUsefulWords(arnab)

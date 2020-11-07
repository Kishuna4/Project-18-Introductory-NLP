import nltk
from nltk import word_tokenize, pos_tag
nltk.download('maxent_ne_chunker')
nltk.download('words')
text = "She went swimming in the ocean."


tokens = word_tokenize(text)
for word in tokens:
    tagged_words = pos_tag(tokens)
print(tagged_words)

NER = nltk.ne_chunk(tagged_words, binary = False)

print(NER)

from nltk.corpus import wordnet

sample_word = wordnet.synsets("can")

for words in sample_word:
    print(words.name())
    print(words.definition())
    print(words.examples())

    for lemma in words.lemmas():
        print(lemma)
    print("/n")

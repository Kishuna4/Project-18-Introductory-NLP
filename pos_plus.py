import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download("averaged_perceptron_tagger")      

text = "I am learning Natural Language Processing Techniques on Coursera."

tokens = word_tokenize(text)
tagged_words = pos_tag(tokens)
print(tagged_words)

grammar = r""" NP: {<.*>+}}<JJ>+{"""

parser = nltk.RegexpParser(grammar)

output = parser.parse(tagged_words)
print(output)
              
putput.draw()

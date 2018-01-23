from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()

string = "First Step in NLTK is tokenizer. tokenizer means divide text data \
into tokens. Here, token means single Entity that is split by any rule for example \
sentence from paragraph."

exa = word_tokenize(string)

for w in exa:
	print(ps.stem(w))

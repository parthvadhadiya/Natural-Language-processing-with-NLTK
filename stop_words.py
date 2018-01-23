from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

exa_sentence = "First Step in NLTK is tokenizer. tokenizer means divide text data \
into tokens. Here, token means single Entity that is split by any rule for example \
sentence from paragraph."

#print(stop_words = set(stopwords.words("english")))



words = word_tokenize(exa_sentence)

filter_sentence = []

filter_sentence.append([w for w in words if w not in stop_words])


print(filter_sentence)

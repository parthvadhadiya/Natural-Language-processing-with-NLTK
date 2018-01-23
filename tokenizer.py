from nltk.tokenize import sent_tokenize, word_tokenize

example_test = "First Step in NLTK is tokenizer. tokenizer means divide text data \
into tokens. Here, token means single Entity that is split by any rule for example \
sentence from paragraph."

print(sent_tokenize(example_test))
print("----------------------------------------------")
print(word_tokenize(example_test))

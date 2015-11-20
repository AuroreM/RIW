corpus = open("cacm.all", "r")
corpus_contenu = corpus.read()
#print(corpus_contenu)
corpus_tokenized = corpus_contenu.split(" ")
#print(corpus_tokenized)

no_punctuation_tokens = []
for token in corpus_tokenized:
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    token = token.replace("\t", "")
    no_punctuation_tokens.append(token)
    
print(no_punctuation_tokens)

#ponctuation_to_remove={"1":",", "2":.}



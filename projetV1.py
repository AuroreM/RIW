#Stocker chaque article de la collection dans un dico
def stockercollection(path):
		documents = {}
		document ={}
		corpus = open(path, "r")
		separateurs = [".T",".W",".B",".A",".N",".X",".K"]
		id = -1

		for line in corpus:
			if (line[0:2] == ".I"):
				if (id <> -1):
					documents[id]=document
					document = {}
				id = int(line[3:])
			elif (line[0:2] in separateurs):
				separateur = line[0:2]
			elif (line[0:2] not in separateurs and id <> -1 and line[0:2] <> ".I"):
				if (separateur in document.keys()):
					if (separateur == ".A"):
						document[separateur] = document[separateur] + [line.replace('\n', '')]
					else:
						document[separateur] = document[separateur] + line.replace('\n','')
				else:
					if (separateur == ".A"):
						document[separateur] = [line.replace('\n', '')]
					else:
						document[separateur] = line.replace('\n','')
		
		documents[id] = document
		return documents

articles = stockercollection("cacm.all")

#print(articles[18].keys())
#print(articles[20].keys())
print(articles[20]['.W'])
#print(len(articles.keys()))


#Stockage des commons words dans un array
fichier_common_words = open("common_words", "r")
common_words_contenu = fichier_common_words.read()
common_tokenized = common_words_contenu.split("\n")

#print(common_tokenized)

def tokenized(path):

	corpus = open(path, "r")
	corpus_contenu = corpus.read()

	corpus_tokenized = corpus_contenu.split(" ")
	no_punctuation_tokens = []
	for token in corpus_tokenized:
	    token = token.replace(".","")
	    token = token.replace(",","")
	    token = token.replace("'", "")
	    token = token.replace(";", "")
	    token = token.replace("\n", "")
	    token = token.replace("\t", "")
	    no_punctuation_tokens.append(token)
	return no_punctuation_tokens

def test_tokenized_article(article):
	if '.W' in article.keys():
		new_article = []
		article['.W'] = article['.W'].split(" ")
		for token in article['.W']:
			token = token.replace(".","")
			token = token.replace(",","")
			token = token.replace("'", "")
			token = token.replace(";", "")
			token = token.replace("\n", "")
			new_article.append(token)
			article['.W'] = new_article
		return article['.W']
	else:
		return -1

print(test_tokenized_article(articles[20]))
print(articles[20]['.W'])

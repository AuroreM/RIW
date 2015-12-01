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

article = stockercollection("cacm.all")

print(article[1][".A"])

#Stockage des commons words dans un array
fichier_common_words = open("common_words", "r")
common_words_contenu = fichier_common_words.read()
common_tokenized = common_words_contenu.split("\n")

print(common_tokenized)

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

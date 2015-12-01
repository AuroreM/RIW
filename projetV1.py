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
						document[separateur] = document[separateur] + [line.replace('\n', ' ')]
					else:
						document[separateur] = document[separateur] + line.replace('\n',' ')
				else:
					if (separateur == ".A"):
						document[separateur] = [line.replace('\n', ' ')]
					else:
						document[separateur] = line.replace('\n',' ')
		
		documents[id] = document
		return documents

#on stocke les articles de notre collection dans le dico articles
articles = stockercollection("cacm.all")

#print(articles[18].keys())
#print(articles[20].keys())
#print(articles[20]['.W'])
#print(len(articles.keys()))

#Stockage des commons words dans un array
fichier_common_words = open("common_words", "r")
common_words_contenu = fichier_common_words.read()
common_tokenized = common_words_contenu.split("\n")

#fonction permettant de tokenizer l'article - stockage dans un tableau
def tokenize_article(article):
	if '.W' in article.keys():
		new_article = []
		article['.W'] = article['.W'].split(" ")
		for token in article['.W']:
			#print(token)
			token = token.lower()
			token = token.replace(".","")
			token = token.replace(",","")
			token = token.replace("'", "")
			token = token.replace(";", "")
			token = token.replace("\n", "")
			new_article.append(token)
		
		return new_article 
	else:
		return -1

def suppr_commonwords_article(article):
	tokenized_article = tokenize_article(article)
	if tokenized_article == -1 :
		return "Pas de resume dans cet article"
	else:
		article_without_common = []
		for token  in tokenized_article:
			if token not in common_tokenized:
				article_without_common.append(token)
		return article_without_common


#print("Traitement texte 20")
#print(len(suppr_commonwords_article(articles[20])))
#print("Traitement texte 1")
#print(suppr_commonwords_article(articles[1]))

def word_and_frequency(tokenized_article):
	frequency_index = {}
	for word in tokenized_article:
		#print word
		if word in frequency_index:
			frequency_index[word] = frequency_index[word] + 1
			#print(frequency_index)
		else:
			frequency_index[word] = 1
			#print(frequency_index)
	return frequency_index

print(len(articles))

tokenized_20 = suppr_commonwords_article(articles[20])
print(tokenized_20)
#print(len(tokenized_20))

print(word_and_frequency(tokenized_20))
# importe puis commande re.findall(r"[\w]", "C'est un test ?!")
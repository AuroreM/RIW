import math

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
#utiliser dans treat_article
def tokenize_article(article):
	new_article = []
	if '.W' in article.keys():
		copy_articleW=article['.W']
		copy_articleW = copy_articleW.split(" ")
		for token in copy_articleW:
			token = token.lower()
			token = token.replace(".","")
			token = token.replace("(","")
			token = token.replace(")","")
			token = token.replace(",","")
			token = token.replace("- ","")
			token = token.replace("'", "")
			token = token.replace(";", "")
			token = token.replace(":", "")
			token = token.replace("\n", "")
			new_article.append(token)
	if '.K' in article.keys():
		copy_articleK = article['.K']
		copy_articleK = copy_articleK.split(" ")
		for token in copy_articleK:
			token = token.lower()
			token = token.replace("(","")
			token = token.replace(")","")
			token = token.replace(".","")
			token = token.replace("- ","")
			token = token.replace(",","")
			token = token.replace("'", "")
			token = token.replace(";", "")
			token = token.replace(":", "")
			token = token.replace("\n", "")
			new_article.append(token)
	if '.T' in article.keys():
		copy_articleT = article['.T']
		copy_articleT = copy_articleT.split(" ")
		for token in copy_articleT:
			token = token.lower()
			token = token.replace(".","")
			token = token.replace(",","")
			token = token.replace("- ","")
			token = token.replace("'", "")
			token = token.replace("(","")
			token = token.replace(")","")
			token = token.replace(";", "")
			token = token.replace(":", "")
			token = token.replace("\n", "")
			new_article.append(token)
	return new_article 

#print(tokenize_article(articles[20]))

#pour tokenizer directement
# importe puis commande re.findall(r"[\w]", "C'est un test ?!")

#Fonction permettant de finir le traitement de l'article (suppression des commonwords)
def treat_article(article):
	tokenized_article = tokenize_article(article)
	if tokenized_article == [] :
		return -1
	else:
		article_without_common = []
		for token  in tokenized_article:
			if token not in common_tokenized:
				article_without_common.append(token)
		return article_without_common

#print("Traitement texte 20")
#print(len(treat_article(articles[20])))
#print("Traitement texte 1")
#print(treat_article(articles[1]))

#Creer un index sur un article {"mot" : freq}
def createIndexArticle(tokenized_article):
	article_frequency_index = {}
	for word in tokenized_article:
		#print word
		if word in article_frequency_index:
			article_frequency_index[word] = article_frequency_index[word] + 1
		else:
			article_frequency_index[word] = 1
	return article_frequency_index

#tokenized_20 = treat_article(articles[20])
#print(createIndexArticle(tokenized_20))

#Creer un index sur un article {"mot" : freqTF}
def createTFIndexArticle(tokenized_article):
	article_frequency_index = {}
	for word in tokenized_article:
		if word in article_frequency_index:
			article_frequency_index[word] = article_frequency_index[word] + 1
		else:
			article_frequency_index[word] = 1
	for token in article_frequency_index:
		article_frequency_index[token] = round(1 + math.log(article_frequency_index[token], 10),2)
	return article_frequency_index

tokenized_20 = treat_article(articles[20])
#print(createTFIndexArticle(tokenized_20))


#index qui renvoie un dictionnaire{"mot" : [{id doc : freq}]}
def createIndex(articles):
	index = {}
	for cle in articles:
		article=articles[cle]
		treated_article = treat_article(article)
		if treat_article(article) <> -1:
			indexArticle=createIndexArticle(treated_article)
			index[cle] = indexArticle
	return index

#print(createIndex(articles))

#index qui renvoie un dictionnaire{"mot" : [{id doc : freqTF}]}
def createTFIndex(articles):
	index = {}
	for cle in articles:
		article=articles[cle]
		treated_article = treat_article(article)
		if treat_article(article) <> -1:
			indexArticle=createTFIndexArticle(treated_article)
			index[cle] = indexArticle
	return index


#index qui renvoie un dictionnaire{"mot" : [{id doc : freq}]}
def createInverseIndex(articles):
	index = {}
	for cle in articles:
		article=articles[cle]
		treated_article = treat_article(article)
		if treat_article(article) <> -1:
			indexArticle=createIndexArticle(treated_article)
			for token in indexArticle:
				if token in index.keys():
					index[token][cle] = indexArticle[token]
				else:
					couple={}
					couple[cle] = indexArticle[token]
					index[token] = couple
	return index

#print(createInverseIndex(articles))
#index = createInverseIndex(articles)
#print(index)

#index qui renvoie un dictionnaire{"mot" : [{id doc : freqTF}]}
def createTFInverseIndex(articles):
	index = {}
	for cle in articles:
		article=articles[cle]
		treated_article = treat_article(article)
		if treat_article(article) <> -1:
			indexArticle=createTFIndexArticle(treated_article)
			for token in indexArticle:
				if token in index.keys():
					index[token][cle] = indexArticle[token]
				else:
					couple={}
					couple[cle] = indexArticle[token]
					index[token] = couple
	return index

#fonction qui renvoie un index sur toute la collection index = {"mot" : freq}
#peut servir pour le calcul de IDF
def createTokenIndex(articles):
	index = {}
	for cle_article in articles:
		article=articles[cle_article]
		if treat_article(article) <> -1:
			treated_article = treat_article(article)
			for token in treated_article:
				if token in index:
					index[token] = index[token] + 1
				else:
					index[token] = 1
	return index

#index= createTokenIndex(articles)
#print(index['parameterization'])


#Creer un index sur un article {"mot" : freqTF}
def createTFIDFIndexArticle(tokenized_article, articles):
	article_frequency_index = {}
	word_frequency = createTokenIndex(articles)
	for word in tokenized_article:
		if word in article_frequency_index:
			article_frequency_index[word] = article_frequency_index[word] + 1
		else:
			article_frequency_index[word] = 1
	for token in article_frequency_index:
		TF = 1 + math.log(article_frequency_index[token], 10)
		freq_word_col = word_frequency[token]
		IDF = math.log((len(articles)/freq_word_col),10)
		article_frequency_index[token] = round(TF*IDF,2)
	return article_frequency_index

#print(createTFIDFIndexArticle(tokenized_20, articles))

"""
A revoir tourne indéfiniment
#index qui renvoie un dictionnaire{"mot" : [{id doc : freqTF}]}
def createTFIDFIndex(articles):
	index = {}
	for cle in articles:
		article=articles[cle]
		treated_article = treat_article(article)
		if treat_article(article) <> -1:
			indexArticle=createTFIDFIndexArticle(treated_article, articles)
			index[cle] = indexArticle
	return index

print(createTFIDFIndex(articles))

""" 
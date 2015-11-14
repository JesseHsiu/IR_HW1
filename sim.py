# -*- coding: UTF-8 -*-
import numpy, heapq, os, logging
from gensim import similarities, corpora, models
from gensim.similarities.docsim import Similarity
import jieba
import jieba.analyse
import xml.etree.ElementTree as ET
import opencc
import string  
import re
from types import *

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
########## CLASSES ##########

class DocCorpus(object):
	def __init__(self, texts, dict):
		self.texts = texts
		self.dict = dict

	def __iter__(self):
		for line in self.texts:
			yield self.dict.doc2bow(line)

class Docs(object):
	def __init__(self, dirname, querys=None):
		self.dirname = dirname
		self.querys = querys

	def __iter__(self):
		for fname in os.listdir(self.dirname):
			with open(os.path.join(self.dirname, fname)) as f:
				s = f.read()
				yield s.split(',')
		if self.querys != None:
			for query in self.querys:
				yield query
	def getDocCount(self):
		return len(os.listdir(self.dirname))
	def getDocNameByID(self, docId):
		return os.listdir(self.dirname)[docId]

class QueryList(object):
	# """docstring for QueryList"""
	def __init__(self, url):
		self.url = url
	def getQuerys(self):
		tree = ET.parse(self.url)
		root = tree.getroot()

		querys = []
		for query in root:
			# print "ok"
			queryDoc = []
			querys.append(queryDoc)
			for doc in query:
				if type(doc) is not ListType:
					for term in jieba.cut(simplify(doc.attrib['title'].rstrip('\n')), cut_all=True):
						queryDoc.append(term)
					if doc[0].text != None:
						for term in jieba.cut(simplify(doc[0].text.rstrip('\n')), cut_all=True):
							queryDoc.append(term)
		return querys
########## FUNCTIONS ##########
def simplify(text):
 return opencc.convert(text, config='t2s.json')

def traditionalize(text):
 return opencc.convert(text, config='zhs2zht.ini').encode('utf8')
		

if __name__ == '__main__':
	

	queryObject = QueryList('./data/query_story.xml')
	querys = queryObject.getQuerys()
	documents = Docs('./data/news_cuts/',querys)
	dictionary = corpora.Dictionary(documents)

	once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq <= 20]
	dictionary.filter_tokens(once_ids)

	dictionary.compactify()

	dictionary.save('./dict.dict')
    # dictionary = Dictionary.load('./dict.dict')
	dc = DocCorpus(documents, dictionary)
	tfidf = models.TfidfModel(dc)

	index = Similarity(corpus=tfidf[dc], num_features=tfidf.num_nnz, output_prefix="shard",num_best=120)

	with open('result.txt', 'w+') as f:
		for query in querys:
			result = index[dictionary.doc2bow(query)]
			print "================="
			for rank in result:
				if rank[0] < documents.getDocCount():
					print documents.getDocNameByID(rank[0]),
					f.write(documents.getDocNameByID(rank[0]) + " ")
			f.write("\n")
    	

	
    		
	
	# print querys[0]

	# for query in querys:
	# 	dictionary = corpora.Dictionary.load('./dict.dict')
	# 	# documents = Docs('./data/news_cuts/')

	# 	index = Similarity.load('./sim.sim')
	# 	# queryDict = corpora.Dictionary([query])
	# 	# dictionary.merge_with(corpora.Dictionary([query]))
	# 	# once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq <= 20]
	# 	# dictionary.filter_tokens(once_ids)

	# 	# dictionary.compactify()
	# 	index.close_shard()
	# 	index.add_documents([dictionary.doc2bow(text) for text in [query]])


	# 	print index.similarity_by_id(0)
			
		# for rank in index.similarity_by_id(len(os.listdir('./data/news_cuts/'))):
		# 	print os.listdir('./data/news_cuts/')[]

	# 	dictionary.merge_with(corpora.Dictionary([query]))
	# 	once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq <= 20]
	# 	dictionary.filter_tokens(once_ids)
	# 	dictionary.compactify()

	# 	dc = DocCorpus(documents, dictionary)
	# 	tfidf = models.TfidfModel(dc)
	# 	index = Similarity(corpus=tfidf[dc], num_features=tfidf.num_nnz, output_prefix="shard",num_best=100)
		# with open('result.txt', 'w+') as the_file:
			# the_file.write(index.similarity_by_id(len(os.listdir('./data/news_cuts/'))+1))
		# print "===========query==========="
		# for rank in index.similarity_by_id(len(os.listdir('./data/news_cuts/'))):
		# 	print os.listdir('./data/news_cuts/')[rank[0]]
		# print "===========query==========="
		# for i in index:
		# 	print heapq.nlargest(5, enumerate(i), key=lambda x: x[1]) # Output is of the format (document index, score)
	    
	



	# saving sim
	# dictionary = corpora.Dictionary.load('./dict.dict')
	# documents = Docs('./data/news_cuts/')
	# # dictionary.merge_with(corpora.Dictionary([query]))
	# once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq <= 20]
	# dictionary.filter_tokens(once_ids)
	# dictionary.compactify()

	# dc = DocCorpus(documents, dictionary)
	# tfidf = models.TfidfModel(dc)
	# index = Similarity(corpus=tfidf[dc], num_features=tfidf.num_nnz, output_prefix="shard",num_best=100)
	# index.save('./sim.sim')




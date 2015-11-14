# -*- coding: UTF-8 -*-
import numpy, os, logging
from gensim import similarities, corpora, models
from gensim.similarities.docsim import Similarity
import jieba
import jieba.analyse
import xml.etree.ElementTree as ET
import opencc
import sys
import codecs
import multiprocessing as mp
from types import *

# Logging from gensim
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

########## CLASSES ##########
class DocCorpus(object):
	def __init__(self, texts, dict):
		self.texts = texts
		self.dict = dict

	def __iter__(self):
		for line in self.texts:
			yield self.dict.doc2bow(line)

class OriginDocs(object):
	def __init__(self, dirname, outputDir):
		self.dirname = dirname
		self.outputDir = outputDir
	def getOutputDir(self):
		return self.outputDir

	def simplifyAllDoc(self):
		if not os.path.exists(self.outputDir):
			os.makedirs(self.outputDir)
		
		pool = mp.Pool(processes=mp.cpu_count())
		for x in os.listdir(self.dirname):
			pool.apply_async(parseFile, args=(x,self.dirname,self.outputDir))
		pool.close()
		pool.join()
		

# Docs 
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

def parseFile(filename, dirname, outputDir):
		tree = ET.parse(os.path.join(dirname, filename))
		root = tree.getroot()
		
		# Title
		title_cuts = jieba.cut(simplify(root[0].attrib['title'].rstrip('\n')), cut_all=True)
		
		# Content
		seg_list = None
		if root[0][0].text != None:
			seg_list = jieba.cut(simplify(root[0][0].text.rstrip('\n')), cut_all=True)
		# Writing Segment files
		with codecs.open(outputDir + "/" + os.path.basename(filename), "w", "utf-8") as f:
			# Get news title.
			for title in title_cuts:
				if title != '':
					f.write(title)
					f.write(',')
			# Content : if there is no content then skip.
			if root[0][0].text != None:
				for seg in seg_list:
					if seg !='':
						f.write(seg)
						f.write(',')
			f.closed

if __name__ == '__main__':

	if len(sys.argv) == 5:
		originDocs_Dir = sys.argv[1]
		outputDocs_Dir = sys.argv[2]
		queryFile = sys.argv[3]
		resultFileName = sys.argv[4]
		
		print "->>Processing Origin Files"
		# # Origin Docs
		originDocs = OriginDocs(originDocs_Dir, outputDocs_Dir)
		originDocs.simplifyAllDoc();
		print "->>Load QueryFile"
		# Load QueryFile
		queryObject = QueryList(queryFile)
		querys = queryObject.getQuerys()

		# Load Merge(Docs, QueryFile)
		documents = Docs(outputDocs_Dir,querys)
		# Build Dict
		dictionary = corpora.Dictionary(documents)
		once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq <= 20]
		dictionary.filter_tokens(once_ids)
		dictionary.compactify()
		# Save or not depends.
		dictionary.save('./dict.dict')
		# Use this if you saved before
		# dictionary = corpora.Dictionary.load('./dict.dict')

	    # TF-IDF calculation
		dc = DocCorpus(documents, dictionary)
		tfidf = models.TfidfModel(dc)

		# Build DocSimilarityMatrix
		index = Similarity(corpus=tfidf[dc], num_features=tfidf.num_nnz, output_prefix="shard",num_best=120)
		index.save('./sim.sim')
		# Use this if you saved before
		# index = Similarity.load('./sim.sim')

		# Writing down result of query
		with open(resultFileName, 'w+') as f:
			queryid = 1
			for query in querys:
				result = index[dictionary.doc2bow(query)]
				f.write("run,id,rel\n")
				f.write("1,"+ str(queryid) +",")
				queryid+=1
				count = 0
				for rank in result:
					if int(rank[0]) < documents.getDocCount() and count < 100:
						docName = documents.getDocNameByID(rank[0])
						f.write(docName.split('.')[0] + " ")
						count+=1
				f.write("\n")
	else:
		print "Please use like 'python sim.py [originDocs_Dir] [outputDocs_Dir] [queryFile] [resultFileName]'"
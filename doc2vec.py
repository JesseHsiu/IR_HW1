# -*- coding: UTF-8 -*-
import gensim, logging, os

class MySentences(object):
	def __init__(self, dirname):
		self.dirname = dirname

	def __iter__(self):
		for fname in os.listdir(self.dirname):
			with open(os.path.join(self.dirname, fname)) as f:
				s = f.read()
				yield s.split(',')

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = MySentences('./data/news_cuts/')
model = gensim.models.Word2Vec(sentences, min_count=20, workers=4)

model.save('./mymodel.model')

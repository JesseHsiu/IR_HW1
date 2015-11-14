# -*- coding: UTF-8 -*-
import gensim, logging, os

model = gensim.models.Word2Vec.load('./mymodel.model')
print model['企业']
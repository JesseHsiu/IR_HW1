import os

# for fname in os.listdir('./data/news_cuts/'):
    # print fname

import numpy, heapq
from gensim import similarities, corpora, models
from gensim.similarities.docsim import Similarity

# ########## CLASSES ##########

class DocCorpus(object):
    # '''
    # This is just the iterator from the tutorial with a couple modifications for cleanliness:
    # http://radimrehurek.com/gensim/tut1.html#corpus-streaming-one-document-at-a-time
    # '''
    def __init__(self, texts, dict):
        self.texts = texts
        self.dict = dict

    def __iter__(self):
        for line in self.texts:
            yield self.dict.doc2bow(line.lower().split())

# ########## MAIN ##########

if __name__ == '__main__':
    # First get documents to test (in this case from the Gensim tutorial)
    documents = ["Human machine interface for lab abc computer applications",
                "A survey of user opinion of computer system response time",
                "The EPS user interface management system",
                "System and human system engineering testing of EPS",
                "Relation of user perceived response time to error measurement",
                "The generation of random binary unordered trees",
                "The intersection graph of paths in trees",
                "Graph minors IV Widths of trees and well quasi ordering",
                "Graph minors A survey"]

    # Load into gensim dictionary object
    dictionary = corpora.Dictionary(line.lower().split() for line in documents)

    # Filtering, stopword removal and other cleaning happens here. In this case, we're only
    # removing words that occur just once, but there's a lot more that could be done.
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
    dictionary.filter_tokens(once_ids)

    # Compact dictionary
    dictionary.compactify()

    # Now create corpus and tfidf model
    dc = DocCorpus(documents, dictionary)
    tfidf = models.TfidfModel(dc)

    # Create and iterate over the similarity matrix. With a document set of size N, this matrix will be
    # N x N, which is normally too large to hold in memory for any N greater than several tens of thousands.
    # As I understand it, Gensim overcomes this problem by using disk storage.
    index = Similarity(corpus=tfidf[dc], num_features=tfidf.num_nnz, output_prefix="shard", num_best=2)
    
    for rank in index[dictionary.doc2bow(documents[8].lower().split())]:
    	print rank[0],
    # for i in index:
    #     # Using nlargest from heapq changes complexity from the O(n * log(n)) of the sorted function
    #     # to O(n * log(k)), which assuming we only want a small K is MUCH faster with huge arrays.
        # for rank in i:
            # print (rank[0]),
        # print ""


#         # heapq.nlargest(5, enumerate(i), key=lambda x: x[1]) # Output is of the format (document index, score)

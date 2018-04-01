__author__ = 'Caitrin'
from gensim.models import Word2Vec
from sklearn.model_selection import GridSearchCV
from gensim.sklearn_api.w2vmodel import W2VTransformer
import numpy as np
#TODO: need to make sure you're optimizing speed




#TODO:
"""
>>> model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
>>> word_vectors = model.wv
Persist the word vectors to disk with:

>>> word_vectors.save(fname)
>>> word_vectors = KeyedVectors.load(fname)
"""

class EBModel:

    def __init__(self, project):
        self.project = project
####################This evaluation part would be edited for final version of output we get#######################
    def precision_at_k(r, k):
        """Score is precision @ k
        Relevance is binary (nonzero is relevant).
        >>> r = [0, 0, 1]
        >>> precision_at_k(r, 1)
        0.0
        >>> precision_at_k(r, 2)
        0.0
        >>> precision_at_k(r, 3)
        0.33333333333333331
        >>> precision_at_k(r, 4)
        Traceback (most recent call last):
            File "<stdin>", line 1, in ?
        ValueError: Relevance score length < k
        Args:
            r: Relevance scores (list or numpy) in rank order
                (first element is the first item)
        Returns:
            Precision @ k
        Raises:
            ValueError: len(r) must be >= k
        """
        assert k >= 1
        r = np.asarray(r)[:k] != 0
        if r.size != k:
            raise ValueError('Relevance score length < k')
        return np.mean(r)

    ####################This evaluation part would be edited for final version of output we get#######################
    def average_precision(r):
        """Score is average precision (area under PR curve)
        Relevance is binary (nonzero is relevant).
        >>> r = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1]
        >>> delta_r = 1. / sum(r)
        >>> sum([sum(r[:x + 1]) / (x + 1.) * delta_r for x, y in enumerate(r) if y])
        0.7833333333333333
        >>> average_precision(r)
        0.78333333333333333
        Args:
            r: Relevance scores (list or numpy) in rank order
                (first element is the first item)
        Returns:
            Average precision
        """
        r = np.asarray(r) != 0
        out = [precision_at_k(r, k + 1) for k in range(r.size) if r[k]]
        if not out:
            return 0.
        return np.mean(out)

    ####################This evaluation part would be edited for final version of output we get#######################
    def MAP(rs):
        """Score is mean average precision
            Relevance is binary (nonzero is relevant).
            >>> rs = [[1, 1, 0, 1, 0, 1, 0, 0, 0, 1]]
            >>> mean_average_precision(rs)
            0.78333333333333333
            >>> rs = [[1, 1, 0, 1, 0, 1, 0, 0, 0, 1], [0]]
            >>> mean_average_precision(rs)
            0.39166666666666666
            Args:
                rs: Iterator of relevance scores (list or numpy) in rank order
                    (first element is the first item)
            Returns:
                Mean average precision
            """
        return np.mean([average_precision(r) for r in rs])

    ####################This evaluation part would be edited for final version of output we get#######################
    def MRR(rs):
        """Score is reciprocal of the rank of the first relevant item
           First element is 'rank 1'.  Relevance is binary (nonzero is relevant).
           Example from http://en.wikipedia.org/wiki/Mean_reciprocal_rank
           >>> rs = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
           >>> mean_reciprocal_rank(rs)
           0.61111111111111105
           >>> rs = np.array([[0, 0, 0], [0, 1, 0], [1, 0, 0]])
           >>> mean_reciprocal_rank(rs)
           0.5
           >>> rs = [[0, 0, 0, 1], [1, 0, 0], [1, 0, 0]]
           >>> mean_reciprocal_rank(rs)
           0.75
           Args:
               rs: Iterator of relevance scores (list or numpy) in rank order
                   (first element is the first item)
           Returns:
               Mean reciprocal rank
           """
        rs = (np.asarray(r).nonzero()[0] for r in rs)
        return np.mean([1. / (r[0] + 1) if r.size else 0. for r in rs])


    def maxSim(self, word, document, w2v):
        cur_max = float("inf")
        for wd in document:
            dis = w2v.wv.distance(word, wd)
            if dis < cur_max:
                cur_max = dis

        return cur_max


    ### CAITRIN THIS IS WHERE YOU ARE: looking at this page: https://radimrehurek.com/gensim/models/word2vec.html
    #to find out how to calculate cosine similarity


    #CURRENTLY DOING THIS
    #where document1 and document2 are lists of words, preprocessed
    """First, for each word w in the
segment T1 we try to identify the word in the segment T2
that has the highest semantic similarity (maxSim(w, T2)),
according to one of the word-to-word similarity measures
described in the following section."""


    #from https://pdfs.semanticscholar.org/1374/617e135eaa772e52c9a2e8253f49483676d6.pdf
    #because we do not want to use their assymetric similarity as we are not computing other ranking algorithms
    def semantic_similarity(self, t1, t2, w2v):

        t1_num = 0.0
        t1_den = 0.0
        for w in t1:
            w_count = t1.count(w)
            t1_num += self.maxSim(w, t2) * w_count
            t1_den += w_count

        t2_num = 0.0
        t2_den = 0.0
        for w in t2:
            w_count = t1.count(w)
            t2_num += self.maxSim(w, t1) * w_count
            t2_den += w_count

        return 0.5(t1_num/t1_den) + (t2_num/t2_den)

    #https://radimrehurek.com/gensim/sklearn_api/w2vmodel.html
    #given our stackoverflow data, we need to create a language model. Stackoverflow data
    #should be in the form of:

   #estimator is our trained w2v model
   #X is validation data
    #y is ground truth data
    #EXCEPT THATS NOT TRUE CAUSE YOURE PROVIDING THE DATA
    def my_scorer(self, estimator, X, y):
        #THIS WILL CALL MAP AND MRR

        #this needs to be a floating point number
        return final_score
    #fulls specs here https://radimrehurek.com/gensim/models/word2vec.html
    def train(self, stackoverflowData):

        #this describes everything you want to search over
        parameters = {'size': [100, 250, 500],
                      'window': [5, 10],
                      'sg': [1],
                      'workers': [16],
                      'hs': [0],
                      'negative': [25],
                      'iter': [1]
                      }

        w2v = W2VTransformer()
        clf = GridSearchCV(w2v, parameters, scoring=self.my_scorer, verbose=2, n_jobs=3)
        clf.fit(stackoverflowData, y=None)

    def test(self, clf, X, y):
        return self.my_scorer(clf, X, y)


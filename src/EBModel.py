__author__ = 'Caitrin'
from gensim.models import Word2Vec
from sklearn.model_selection import GridSearchCV
from gensim.sklearn_api.w2vmodel import W2VTransformer
#TODO: need to make sure you're optimizing speed


class EBModel:

    def __init__(self, project):
        self.project = project



    def maxSim(self, word, document, w2v):
        pass
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


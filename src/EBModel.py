__author__ = 'Caitrin'
from gensim.models import Word2Vec
from sklearn.model_selection import GridSearchCV
from gensim.sklearn_api.w2vmodel import W2VTransformer
#TODO: need to make sure you're optimizing speed


class EBModel:

    def __init__(self, project):
        self.project = project

    #CURRENTLY DOING THIS
    def asymmetric_similarity(self):
        pass

    #https://radimrehurek.com/gensim/sklearn_api/w2vmodel.html
    #given our stackoverflow data, we need to create a language model. Stackoverflow data
    #should be in the form of:

   #estimator is our trained w2v model
   #X is validation data
    #y is ground truth data
    def my_scorer(self, estimator, X, y):


        #this needs to be a floating point number
        return final_score
    #fulls specs here https://radimrehurek.com/gensim/models/word2vec.html
    def train(self):

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
        return clf

    def test(self, clf, X, y):
        return self.my_scorer(clf, X, y)


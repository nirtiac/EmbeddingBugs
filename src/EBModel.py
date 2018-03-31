__author__ = 'Caitrin'
from gensim.models import Word2Vec
from sklearn.model_selection import GridSearchCV
from gensim.sklearn_api.w2vmodel import W2VTransformer
#TODO: need to make sure you're optimizing speed


class EBModel:

    def __init__(self, project):
        self.project = project


    #https://radimrehurek.com/gensim/sklearn_api/w2vmodel.html
    #given our stackoverflow data, we need to create a language model. Stackoverflow data
    #should be in the form of:


    #fulls specs here https://radimrehurek.com/gensim/models/word2vec.html
    def train(self, parameter_set):
        pass

    def test(self):
        pass

    def evaluate(self):
        pass

    #use http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV
    #find the optimal hyperparameter settings, given the evaluation and the train
    def optimize(self):
        pass

    def asymmetric_similarity(self):
        pass

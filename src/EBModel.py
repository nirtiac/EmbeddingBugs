__author__ = 'Caitrin'
import gensim
from sklearn.model_selection import GridSearchCV
from gensim.sklearn_api.w2vmodel import W2VTransformer
import numpy as np
from preprocessingCodeLang import Preprocessor
from DataProcessor import DataProcessor
#TODO: need to make sure you're optimizing speed
import os



#TODO:
"""
>>> model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
>>> word_vectors = model.wv
Persist the word vectors to disk with:

>>> word_vectors.save(fname)
>>> word_vectors = KeyedVectors.load(fname)
"""

class EBModel:

    def __init__(self, path_to_stackoverflow_data, path_to_reports_data, path_to_starter_repo, path_to_processed_repo, path_to_temp, train_split_index_start, train_split_index_end, final_model, project, accuracy_at_k_value=10,):
        self.path_to_stackoverflow_data = path_to_stackoverflow_data
        self.path_to_reports_data = path_to_reports_data
        self.path_to_starter_repo = path_to_starter_repo
        self.path_to_processed_repo = path_to_processed_repo
        self.path_to_temp = path_to_temp
        self.train_split_index_start = train_split_index_start
        self.train_split_index_end = train_split_index_end
        self.final_model = final_model
        self.project = project
        self.accuracy_at_k_value = accuracy_at_k_value

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
        k = self.accuracy_at_k_value
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
            t1_num += self.maxSim(w, t2, w2v) * w_count
            t1_den += w_count

        t2_num = 0.0
        t2_den = 0.0
        for w in t2:
            w_count = t1.count(w)
            t2_num += self.maxSim(w, t1, w2v) * w_count
            t2_den += w_count

        return 0.5(t1_num/t1_den) + (t2_num/t2_den)

    #returns ranked set of all files, by their path relative to the root folder
    def compare_all_files(self, file_path, report_text, estimator):
        scoring = {}
        for dir_, _, files in os.walk(file_path):
            for fileName in files:
                relDir = os.path.relpath(dir_, file_path)
                relFile = os.path.join(relDir, fileName)
                full_path = file_path + relFile
                with open(full_path, 'r') as content_file:
                    content = content_file.readlines() #TODO: put this into separate lists if not already done
                    l_content = []
                    for line in content:
                        l = line.split(",")
                        l_content.append(l)

                score = self.semantic_similarity(l_content, report_text, estimator)
                scoring[relFile] = score
        sorted_scoring = sorted(scoring.items(), key=operator.itemgetter(0))

        return sorted_scoring


    #NOTE: we're choosing precision@k where k=10
    def call_MAP(self, estimator):
        dp = DataProcessor()

        already_processed = False
        previous_commit = None
        all_scores = []

        #TODO: define path to workbook
        reports = dp.read_and_process_report_data(self.path_to_reports_data, self.project)
        for report in reports[self.train_split_index_start: self.train_split_index_end]:
            report_text = report.processed_description
            if not already_processed:
                dp.create_file_repo(self.path_to_starter_repo, report, self.path_to_processed_repo)
                already_processed = True
                previous_commit = report.commit
            else:
                dp.update_file_repo(previous_commit, report.commit, self.path_to_starter_repo, self.path_to_temp, self.path_to_processed_repo)
                previous_commit = report.commit

            #where the file comes first, then the score, sorted by score
            sorted_scoring = self.compare_all_files(self.path_to_processed_repo, report_text, estimator)

            scoring_matrix = []
            for t in sorted_scoring[:self.accuracy_at_k_value]:
                if unicode(t[0], "utf-8") in report.files: #TODO: check here that unicode isn't causing an issue. if it is. fix.
                    scoring_matrix.append(1)
                else:
                    scoring_matrix.append(0)

            all_scores.append(scoring_matrix)

        final_score = MAP(all_scores)
        return final_score

    def call_MRR(self, estimator, X, y):

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

        dp = DataProcessor()
        #data = dp.get_stackoverflow_data(self.path_to_stackoverflow_data)
        w2v = W2VTransformer()
        #TODO: confirm that you want to use MAP to construct the best_scoring parameter
        #TODO: if none for CV doesn't work then you're going to have to run grid search manually with multiprocessing module
        # see: https://stackoverflow.com/questions/44636370/scikit-learn-gridsearchcv-without-cross-validation-unsupervised-learning/44682305#44682305
        #clf = GridSearchCV(w2v, parameters, scoring={"MPP": self.call_MRR, "MAP": self.call_MAP}, verbose=2, n_jobs=3, refit="MAP", cv=[(slice(None), slice(None))])

        #current implementation version only usees MAP to score
        #TODO:fix map, as it that was a leftover of hwaving two scoring functions

        #TODO: put back n_jobs
        #cv=[(slice(None), slice(None))]
        #clf = GridSearchCV(w2v, parameters, scoring= self.call_MAP, verbose=2)
        cur_max = 0
        best_model = None
        for s in parameters["size"]:
            for w in parameters["window"]:
                model = gensim.models.Word2Vec(sentences=data, sg=1, size=s, window=w, workers=16, hs=0, negative=25, iter=1)
                score = call_MAP()
                if score > cur_max:
                    cur_max = score
                    best_model = model

        #clf.fit(data, y=None)

        #TODO: or perhaps actually return the best_estimator attribute? although you can call predict directly

        #TODO: make sure you're saving this!!!
        m = clf.best_estimator_
        word_vectors = model.wv
        word_vectors.save(self.final_model)
        return clf

    def test(self, clf, X, y):
        return self.my_scorer(clf, X, y)


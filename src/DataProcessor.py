__author__ = 'Caitrin'
import os
import itertools

class DataProcessor.py:

    def __init__(self):
        pass


    def get_stackoverflow_data(self, directory):
        sent = []
        for f_path in os.listdir(directory):
            with open(f_path, 'r') as content_file:
                content = content_file.read()
                tokens = content.split()
                code = [s for s in tokens if "@" in s]
                nl = [s for s in tokens if "@" not in s]
                sent.extend([zip(x, nl) for x in itertools.permutations(code, len(nl))])
                sent.append(tokens)

        return sent


#Gensim expects input of tokenized sentences as shown below

#sentences = [[‘This’, ‘is’, ‘the’, ‘first’, ‘sentence’], [‘This’, ‘is’, ‘the’, ‘second’, ‘sentence’], [‘This’, ‘is’, ‘the’, ‘third’, ‘sentence’]]


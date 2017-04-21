import pandas as pd
from sklearn.utils import shuffle
from sklearn import svm
from sklearn.linear_model import LogisticRegression
import functools as ft
import numpy as np
from sklearn.model_selection import KFold
from sklearn import datasets
import random
from sklearn.model_selection import ShuffleSplit
from sklearn.naive_bayes import GaussianNB

# nos imports
from entity.dataset import Dataset
from .constants import ALGORITHMS

class Algorithm():

    def __init__(self, algo):
        try:
            self.algorithm = ALGORITHMS[algo]
        except KeyError:
        # except (KeyError, ValueError) as e:
            print("l'algo renseigné '" + algo + "' n'existe pas")
            exit()

        self.dataset = None
        self.avg_score = None
        self.trained_versions = []
        self.scores_cross_validation_app = []
        self.scores_cross_validation_test = []
        self.avg_score = None

    def train_algorithm(self, x_train, y_train):
        self.trained_versions.append(self.algorithm.fit(x_train, y_train))
        return self.trained_versions[-1]

    def evaluate_test_data(self, trained_algorithm, x_test, y_test):
        score = trained_algorithm.score(x_test, y_test)
        return score

    def train_on_dataset(self, dataset):
        self.dataset = dataset

        train_indexes_table = self.dataset.train_indexes_table
        test_indexes_table = self.dataset.test_indexes_table
        for i in range(0, len(train_indexes_table)):

            trained_algo = self.train_algorithm(
                self.dataset.data[train_indexes_table[i],],
                self.dataset.label[train_indexes_table[i]]
            )

            score_app = self.evaluate_test_data(
                trained_algo,
                self.dataset.data[train_indexes_table[i]],
                self.dataset.label[train_indexes_table[i]]
            )
            self.scores_cross_validation_app.append(score_app)

            score_test = self.evaluate_test_data(
                trained_algo,
                self.dataset.data[test_indexes_table[i]],
                self.dataset.label[test_indexes_table[i]]
            )
            self.scores_cross_validation_test.append(score_test)

        self.avg_score = np.mean(self.scores_cross_validation_test)
        print("average score: "+str(self.avg_score))

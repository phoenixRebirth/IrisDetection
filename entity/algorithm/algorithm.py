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

# our imports
from .constants import ALGORITHMS_TYPE
from entity.dataset import Dataset
from .train_case import TrainCase

class Algorithm():

    def __init__(self, algo, *args, **kwargs):
        try:
            self.algorithm = ALGORITHMS_TYPE[algo](kwargs)
        except KeyError:
            print("the algorithm '" + algo + "' is not recognized")
            exit()

        self.dataset = None
        self.avg_score = None
        self.train_cases = []

    def reinitialize(self):
        self.train_cases = [] # garbage collector will delete the train_cases automatically
        self.avg_score = None
        self.dataset = None

    def train_on_dataset(self, dataset):
        self.reinitialize()
        self.dataset = dataset

        train_indexes_table = self.dataset.train_indexes_table
        test_indexes_table = self.dataset.test_indexes_table
        for i in range(0, len(train_indexes_table)):
            train_case = TrainCase(self, train_indexes_table[i], test_indexes_table[i])
            train_case.train_algorithm()
            self.train_cases.append(train_case)

    def calculate_score(self):
        self.avg_score = np.mean([train_case.test_score for train_case in self.train_cases])
        return self.avg_score

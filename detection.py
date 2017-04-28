import sys
import pandas as pd
from sklearn.utils import shuffle
from sklearn import svm
from sklearn.linear_model import LogisticRegression
import functools as ft
import numpy as np
from sklearn.model_selection import KFold
import random
from sklearn.model_selection import ShuffleSplit
from sklearn.naive_bayes import GaussianNB

from entity import Dataset, Algorithm
from config import DEFAULT_SAMPLE_NUMBER, DEFAULT_TEST_PROPORTION
import parser

def setup_config(sys_args):
    arguments = parser.parse_sys_args(sys_args)

    try:
        n_samples = int(arguments['n'])
    except (ValueError, KeyError) as e :
        n_samples = DEFAULT_SAMPLE_NUMBER
        print('No sample number provided. Using '+str(DEFAULT_SAMPLE_NUMBER)+' instead.')
    print('Running algorithm with '+str(n_samples)+' samples')

    try:
        test_proportion = float(arguments['p'])
    except (ValueError, KeyError) as e :
        test_proportion = DEFAULT_TEST_PROPORTION
        print('No test proportion provided. Using '+str(DEFAULT_TEST_PROPORTION)+' instead.')
    print('Running algorithm with '+str(test_proportion)+' as test proportion')

    return n_samples, test_proportion


if __name__ == '__main__':
    n_samples, test_proportion = setup_config(sys.argv)

    iris_set = Dataset.import_data_from_sklearn()
    iris_set.generate_train_test_indexes(n_samples, test_proportion)

    C_range = [0.1*(i+1) for i in range(0, 10)]
    output = []
    for c in C_range:
        svm = Algorithm('svm', C = c)
        svm.train_on_dataset(iris_set)
        score = svm.calculate_score()
        output.append(score)
        print(score)
        svm.reinitialize()

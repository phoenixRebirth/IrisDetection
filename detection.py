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
import copy

from entity import Dataset, Algorithm, InputParameters
from config import DEFAULT_SAMPLE_NUMBER, DEFAULT_TEST_PROPORTION
import service.parser as parser

def extract_config_path(sys_args):
    arguments = parser.parse_sys_args(sys_args)

    try:
        conf_path = arguments['conf']
    except KeyError :
        print('No config file provided. Please type "conf=myfile"')
        exit()

    return conf_path

if __name__ == '__main__':
    config_path = extract_config_path(sys.argv)
    input_parameters = InputParameters.import_parameters_from_file(config_path)

    iris_set = Dataset.import_data_from_file(input_parameters.dataset_path)
    iris_set.generate_train_test_indexes(input_parameters.sample_number, input_parameters.test_proportion)

    inputs = input_parameters.algos
    outputs = []

    for input_algo in inputs:
        algo_type = input_algo['type']
        params = input_algo.get('params', {})
        algo = Algorithm(algo_type, **params)
        algo.train_on_dataset(iris_set)

        algo_details_output = copy.deepcopy(input_algo)
        algo_details_output['score'] = algo.calculate_score()
        outputs.append(algo_details_output)

        algo.reinitialize()

    print('\n')
    print('Results: ')
    for output in outputs:
        print(output)

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

#0 Data processing¶

# set random generator seed
# random.seed(20170312)

# input:
# output:
#   List of List (nbr data = nbr rows, nbr parameters = nbr cols):  X
#   List (nbr data = nbr elements):                                 Y
def import_data():
    dataset = datasets.load_iris()
    return dataset.data, dataset.target


def split_train_test(x, y, nb_training_data):
    nb_data = len(x)
    indexes = shuffle(range(0,nb_data))

    x_train = iris_df.data[indexes[:nb_training_data], ]
    y_train = iris_df.target[indexes[:nb_training_data]]
    x_test = iris_df.data[indexes[nb_training_data:], ]
    y_test = iris_df.target[indexes[nb_training_data:]]

    return x_train, x_test, y_train, y_test

def train_algorithm(algorithm, x_train, y_train):
    trained_algorithm = algorithm.fit(x_train, y_train)
    print('Train precision: '+ trained_algorithm.score(x_train, y_train))
    return trained_algorithm

def evaluate_test_data(trained_algorithm, x_test, y_test):


algorithm = LogisticRegression(solver='newton-cg', max_iter=100, random_state=42, multi_class='multinomial')

train_precision = trained_algorithm.score(x_train, y_train)

y_pred = trained_algorithm.predict(x_test)
test_precision = trained_algorithm.score(x_test, y_test)

#
# # 2 Cross-validations
#
# apps = pd.DataFrame(0., index=np.arange(10), columns=["logreg", "svm", "NB"])
# tests = pd.DataFrame(0., index=np.arange(10), columns=["logreg", "svm", "NB"])
#
#
# ss = ShuffleSplit(n_splits=10, random_state=0)
# i = 0
# for train_index, test_index in ss.split(iris_df.target):
#     logreg_clf = LogisticRegression(solver='newton-cg', max_iter=100, random_state=42,
#                              multi_class='multinomial').fit(iris_df.data[train_index,], iris_df.target[train_index])
#     svm_clf = svm.SVC(decision_function_shape='ovo').fit(iris_df.data[train_index,], iris_df.target[train_index])
#     nb_clf = GaussianNB().fit(iris_df.data[train_index,], iris_df.target[train_index])
#     apps["logreg"][i] = logreg_clf.score(iris_df.data[train_index,], iris_df.target[train_index])
#     tests["logreg"][i] = logreg_clf.score(iris_df.data[test_index], iris_df.target[test_index])
#     apps["svm"][i] = svm_clf.score(iris_df.data[train_index,], iris_df.target[train_index])
#     tests["svm"][i] = svm_clf.score(iris_df.data[test_index], iris_df.target[test_index])
#     apps["NB"][i] = nb_clf.score(iris_df.data[train_index,], iris_df.target[train_index])
#     tests["NB"][i] = nb_clf.score(iris_df.data[test_index], iris_df.target[test_index])
#     i = i + 1
#
#
# apps = 1. - apps
# apps
#
# # std training error
# np.std(apps)
#
# # rule of thumb : minimize the average error + 1 std => svm is still the best model
# np.mean(apps) + np.std(apps)
#
# # Naive Bayes works not very well because of strong theorical hypotheses (features independence)
# # which is not intuitively met in this case.
# # SVM work better than logistic regression because of the kernel transformation
#
#
#
#
#
#
#
#

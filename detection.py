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

from entity import Dataset, Algorithm

def import_data_from_sklearn():
    dataset = datasets.load_iris()
    return Dataset(dataset.data, dataset.target)

if __name__ == '__main__':
    iris_set = import_data_from_sklearn()
    iris_set.generate_train_test_indexes(10, 0.1)

    svm = Algorithm('svm')
    svm.train_on_dataset(iris_set)
    score = svm.calculate_score()
    print(score)
    svm.reinitialize()

    # print("score cross validation sur apprentissage:")
    # print(scores_cross_validation_app)
    # print("mean score cross validation sur apprentissage:")
    # print(np.mean(scores_cross_validation_app))
    # print("std score cross validation sur apprentissage:")
    # print(np.std(scores_cross_validation_app))
    # print("score cross validation sur test:")
    # print(scores_cross_validation_test)
    # print("mean score cross validation sur test:")
    # print(np.mean(scores_cross_validation_test))
    # print("std score cross validation sur test:")
    # print(np.std(scores_cross_validation_test))
    # print("mean score + std score cross validation sur test:")
    # print(np.mean(scores_cross_validation_test) + np.std(scores_cross_validation_test))
    # print("std score cross validation sur test:")



# def main(argv = None):
#     print("jespère que tu as raison")
#     return 0
#
#     if __name__ == "__main__":
#         print("jespère que tu as raison")
#         return 0
#         sys.exit(main())


#
# # 2 Cross-validations
#
# apps = pd.DataFrame(0., index=np.arange(10), columns=["logreg", "svm", "NB"])
# tests = pd.DataFrame(0., index=np.arange(10), columns=["logreg", "svm", "NB"])
#
#
# ss = ShuffleSplit(n_splits=10, random_state=0)
# i = 0
# for train_indexes, test_indexes in ss.split(iris_df.target):
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

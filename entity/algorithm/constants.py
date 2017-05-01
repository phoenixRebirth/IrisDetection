from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

ALGORITHMS_TYPE = {
    'svm': lambda x : svm.SVC(decision_function_shape='ovo', **x),
    'LogisticRegression': lambda x : LogisticRegression(solver='newton-cg', max_iter=100, random_state=42, multi_class='multinomial', **x),
    'NaiveBayes': lambda x : GaussianNB(**x)
}

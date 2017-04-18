from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

ALGORITHMS = {
    'svm': svm.SVC(decision_function_shape='ovo'),
    'LogisticRegression': LogisticRegression(solver='newton-cg', max_iter=100, random_state=42, multi_class='multinomial'),
    'NaïveBayes': GaussianNB()
}

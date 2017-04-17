from sklearn.model_selection import ShuffleSplit

class Dataset():
    # args est le tableau des paramètres supplémentaires(en option(*))
    # kwargs est le dico des paramètres supplémentaires(en option(*))
    # les paramètres de la forme a = 'quelque chose' sont stockés dans kwargs
    # les paramètres non nommés sont stockés dans args
    # notion d'odre = tableau
    # notion d'association = dico (un dico n'a pas d'ordre)

    def __init__(self, data, label, *args, **kwargs):
        self.data = data
        self.label = label

    def train_algorithm(self, algorithm, x_train, y_train):
        trained_algorithm = algorithm.fit(x_train, y_train)
        return trained_algorithm

    def evaluate_test_data(self, trained_algorithm, x_test, y_test):
        score = trained_algorithm.score(x_test, y_test)
        return score

    def cross_validations (self, algorithm, n_splits, test_size):
        scores_cross_validation_app = []
        scores_cross_validation_test = []
        ss = ShuffleSplit(n_splits=n_splits, random_state=0, test_size = test_size)

        # splits = ss.split(y)
        # for split in splits:
        #     train_indexes = split[0]
        #     test_indexes = split[1]

        for train_indexes, test_indexes in ss.split(self.label):
            trained_algo = self.train_algorithm(algorithm, self.data[train_indexes,], self.label[train_indexes])
            score_app = self.evaluate_test_data(trained_algo, self.data[train_indexes], self.label[train_indexes])
            score_test = self.evaluate_test_data(trained_algo, self.data[test_indexes], self.label[test_indexes])
            # scores_cross_validation[i] = score
            scores_cross_validation_app.append(score_app)
            scores_cross_validation_test.append(score_test)
        return scores_cross_validation_app, scores_cross_validation_test

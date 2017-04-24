class TrainCase():
    def __init__(self, reference_algorithm, train_indexes, test_indexes, *args, **kwargs):
        self.reference_algorithm = reference_algorithm
        self.trained_algorithm = None
        self.train_indexes = train_indexes
        self.test_indexes = test_indexes
        self.train_score = None
        self.test_score = None

    def train_algorithm(self):
        x_train = self.reference_algorithm.dataset.data[self.train_indexes,]
        y_train = self.reference_algorithm.dataset.label[self.train_indexes]
        self.trained_algorithm = self.reference_algorithm.algorithm.fit(x_train, y_train)

        self.evaluate_algorithm_on_train()
        self.evaluate_algorithm_on_test()

    def evaluate_algorithm_on_test(self):
        x_test = self.reference_algorithm.dataset.data[self.test_indexes,]
        y_test = self.reference_algorithm.dataset.label[self.test_indexes]
        self.test_score = self.trained_algorithm.score(x_test, y_test)

    def evaluate_algorithm_on_train(self):
        x_train = self.reference_algorithm.dataset.data[self.train_indexes,]
        y_train = self.reference_algorithm.dataset.label[self.train_indexes]
        self.train_score = self.trained_algorithm.score(x_train, y_train)

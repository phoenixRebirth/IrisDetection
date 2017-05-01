from sklearn.model_selection import ShuffleSplit
from sklearn import datasets

class Dataset():

    def __init__(self, data, label, *args, **kwargs):
        self.data = data
        self.label = label
        self.shuffle_split = None
        self.train_indexes_table =[]
        self.test_indexes_table =[]

    def generate_train_test_indexes(self, n_splits, test_proportion, random_state = 0):
        self.shuffle_split = ShuffleSplit(n_splits = n_splits, random_state = random_state, test_size = test_proportion)
        for train_indexes, test_indexes in self.shuffle_split.split(self.label):
            self.train_indexes_table.append(train_indexes)
            self.test_indexes_table.append(test_indexes)


    @staticmethod
    def import_data_from_sklearn():
        dataset = datasets.load_iris()
        return Dataset(dataset.data, dataset.target)

    @staticmethod
    def import_data_from_file(filename):
        print('this function is not supported yet')
        exit()

from sklearn.model_selection import ShuffleSplit
from sklearn import datasets
import numpy

import service.file_reader as file_reader

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
        # TODO : import directly data into numpy array
        # TODO : manage numpy.array conversion error
        parsed_data = file_reader.open_json(filename)
        try:
            data = parsed_data['data']
            label = parsed_data['label']
        except KeyError as e:
            print('File is missing '+str(e)+' information')
            exit()

        return Dataset(numpy.array(data), numpy.array(label))

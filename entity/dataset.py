from sklearn.model_selection import ShuffleSplit
from sklearn import datasets
import numpy

import service.file_reader as file_reader
import service.network as network

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
    def import_data_from_file_or_api(filename, use_api):
        if (use_api):
            parsed_data = Dataset.get_json_data_from_api(filename)
        else:
            parsed_data = Dataset.get_json_data_from_file(filename)


        # TODO : import directly data into numpy array
        # TODO : manage numpy.array conversion error
        try:
            data = parsed_data['data']
            label = parsed_data['label']
        except KeyError as e:
            print('File is missing '+str(e)+' information')
            exit()

        return Dataset(numpy.array(data), numpy.array(label))

    @staticmethod
    def get_json_data_from_file(filename):
        return file_reader.open_json(filename)

    @staticmethod
    def get_json_data_from_api(url):
        return network.get_url_content_as_json(url)


from sklearn.model_selection import ShuffleSplit
from sklearn import datasets
import numpy

import service.file_reader as file_reader
import service.network as network
import service.database_reader as database_reader

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
    def import_data_from_json(parsed_data):
        # TODO : import directly data into numpy array
        # TODO : manage numpy.array conversion error
        try:
            data = parsed_data['data']
            label = parsed_data['label']
        except KeyError as e:
            print('File is missing ' + str(e) + ' information')
            exit(-1)

        return Dataset(numpy.array(data), numpy.array(label))

    @staticmethod
    def import_data_from_sklearn():
        dataset = datasets.load_iris()
        return Dataset(dataset.data, dataset.target)

    @staticmethod
    def import_data(filename, dataset_type, params):
        if (dataset_type == "api"):
            parsed_data = Dataset.get_json_data_from_api(filename)
            return Dataset.import_data_from_json(parsed_data)
        elif (dataset_type == "db"):
            return Dataset.import_data_from_db(filename, params)
        elif (dataset_type is None):
            parsed_data = Dataset.get_json_data_from_file(filename)
            return Dataset.import_data_from_json(parsed_data)
        else:
            print("unknown dataset type")
            exit(-1)

    @staticmethod
    def get_json_data_from_file(filename):
        return file_reader.open_json(filename)

    @staticmethod
    def get_json_data_from_api(url):
        return network.get_url_content_as_json(url)

    @staticmethod
    def import_data_from_db(database_path, params):
        try:
            iris_table = params['iris_table']
            label_table = params['label_table']
        except KeyError as e:
            print('Dataset is missing '+str(e)+' information')
            exit(-1)

        data_base_connector = database_reader.DatabaseConnector(database_path)
        result = data_base_connector.retrieve_all_data_with_join(
            iris_table, label_table, ("label_id", "id"),
            fields = ['coord_0', 'coord_1', 'coord_2', 'coord_3', 'value']
        )

        label = numpy.empty((len(result), ))
        data = numpy.empty([len(result), 4])
        for i, elt in enumerate(result):
            label[i] = elt[4]
            # label.append(elt[4])
            # data.append([elt[i] for i in range(0, 4)])
            data[i] = [elt[i] for i in range(0, 4)]

        return Dataset(data, label)

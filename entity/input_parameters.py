import service.file_reader as file_reader
from config import DEFAULT_SAMPLE_NUMBER, DEFAULT_TEST_PROPORTION

class InputParameters():

    def __init__(self, sample_number, test_proportion, dataset_path, algos, dataset_type = None, *args, **kwargs):
        self.sample_number = sample_number
        self.test_proportion = test_proportion
        self.dataset_path = dataset_path
        self.dataset_type = dataset_type
        self.algos = algos

    @staticmethod
    def import_parameters_from_file(filename, command_arguments):
        parsed_data = file_reader.open_json(filename)
        try:
            dataset_info = parsed_data['dataset']
            dataset_path = dataset_info.get('path', None)
            dataset_type = dataset_info.get('type', None)

            algos = parsed_data['algos']
        except KeyError as e:
            print('File is missing '+str(e)+' information')
            exit(-1)

        if (dataset_path is None):
            print("no path specified in the 'dataset' config")
            exit(-1)

        try:
            sample_number = command_arguments['n'] if 'n' in command_arguments \
                else parsed_data['sample_number']
            sample_number = int(sample_number)

            print('Using '+str(sample_number)+' as sample number.')
        except (ValueError, KeyError):
            sample_number = DEFAULT_SAMPLE_NUMBER
            print('No/wrong sample number provided. Using '+str(DEFAULT_SAMPLE_NUMBER)+' instead.')

        try:
            test_proportion = command_arguments['p'] if 'p' in command_arguments \
                else parsed_data['test_proportion']
            test_proportion = float(test_proportion)
            print('Using '+str(test_proportion)+' as test proportion.')
        except (ValueError, KeyError):
            test_proportion = DEFAULT_TEST_PROPORTION
            print('No/wrong test proportion provided. Using '+str(DEFAULT_TEST_PROPORTION)+' instead.')

        if type(algos) != list:
            print('Algos must be a list')
            exit(-1)

        for a in algos:
            if (type(a) != dict):
                print('Algos must be a list')
                exit(-1)

            if 'type' not in a:
                print('Algos must have a "type" key')
                exit(-1)

        return InputParameters(sample_number, test_proportion, dataset_path, algos, dataset_type)

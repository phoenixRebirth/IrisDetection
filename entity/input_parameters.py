import service.file_reader as file_reader

class InputParameters():

    def __init__(self, sample_number, test_proportion, dataset_path, algos, *args, **kwargs):
        self.sample_number = sample_number
        self.test_proportion = test_proportion
        self.dataset_path = dataset_path
        self.algos = algos

    @staticmethod
    def import_parameters_from_file(filename):
        parsed_data = file_reader.open_json(filename)
        try:
            sample_number = parsed_data['sample_number']
            test_proportion = parsed_data['test_proportion']
            dataset_path = parsed_data['dataset_path']
            algos = parsed_data['algos']
        except KeyError as e:
            print('File is missing '+str(e)+' information')
            exit()

        try:
            sample_number = int(sample_number)
        except ValueError:
            sample_number = DEFAULT_SAMPLE_NUMBER
            print('No/wrong sample number provided. Using '+str(DEFAULT_SAMPLE_NUMBER)+' instead.')

        try:
            test_proportion = float(test_proportion)
        except ValueError:
            test_proportion = DEFAULT_TEST_PROPORTION
            print('No/wrong test proportion provided. Using '+str(DEFAULT_TEST_PROPORTION)+' instead.')

        if type(algos) != list:
            print('algos must be a list')
            exit()

        for a in algos:
            if (type(a) != dict):
                print('algos must be a list')
                exit()

            if 'type' not in a:
                print('algos must have a "type" key')
                exit()

        return InputParameters(sample_number, test_proportion, dataset_path, algos)

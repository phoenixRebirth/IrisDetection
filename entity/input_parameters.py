import service.file_reader as file_reader
from config import DEFAULT_SAMPLE_NUMBER, DEFAULT_TEST_PROPORTION

class InputParameters():

    def __init__(self, sample_number, test_proportion, dataset_path, algos, use_api = False, *args, **kwargs):
        self.sample_number = sample_number
        self.test_proportion = test_proportion
        self.dataset_path = dataset_path
        self.use_api = use_api
        self.algos = algos

    @staticmethod
    def import_parameters_from_file(filename, command_arguments):
        parsed_data = file_reader.open_json(filename)
        try:
            dataset_path = parsed_data['dataset_path']
            algos = parsed_data['algos']
        except KeyError as e:
            print('File is missing '+str(e)+' information')
            exit()

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
            exit()

        for a in algos:
            if (type(a) != dict):
                print('Algos must be a list')
                exit()

            if 'type' not in a:
                print('Algos must have a "type" key')
                exit()

        use_api = parsed_data.get('use_api', False)

        return InputParameters(sample_number, test_proportion, dataset_path, algos, use_api)

import sys
import copy

from entity import Dataset, Algorithm, InputParameters
import service.parser as parser

def extract_system_arguments(sys_args):
    arguments = parser.parse_sys_args(sys_args)
    try:
        conf_path = arguments.pop('conf')
    except KeyError:
        print('No config file provided. Please type "conf=myfile"')
        exit()

    return conf_path, arguments

if __name__ == '__main__':
    config_path, command_arguments = extract_system_arguments(sys.argv)
    input_parameters = InputParameters.import_parameters_from_file(config_path, command_arguments)

    iris_set = Dataset.import_data(input_parameters.dataset_path, input_parameters.dataset_type, input_parameters.dataset_params)
    iris_set.generate_train_test_indexes(input_parameters.sample_number, input_parameters.test_proportion)

    inputs = input_parameters.algos
    outputs = []

    for input_algo in inputs:
        algo_type = input_algo['type']
        params = input_algo.get('params', {})
        algo = Algorithm(algo_type, **params)
        algo.train_on_dataset(iris_set)

        algo_details_output = copy.deepcopy(input_algo)
        algo_details_output['score'] = algo.calculate_score()
        outputs.append(algo_details_output)

        algo.reinitialize()

    print('\n')
    print('Results: ')
    for output in outputs:
        print(output)

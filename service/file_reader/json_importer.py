import json

def open_json(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print('File ' + filename + ' not found')
        exit()

    data = f.read()

    try:
        parsed_data = json.loads(data)
    except json.decoder.JSONDecodeError as e:
        print('Could not read file:\n' + str(e))
        exit()

    return parsed_data

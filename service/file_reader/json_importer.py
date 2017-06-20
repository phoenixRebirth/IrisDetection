import json
import os

def read_json(data):
    try:
        parsed_data = json.loads(data)
    except json.decoder.JSONDecodeError as e:
        print('Could not read content as json:\n' + str(e))
        exit(-1)

    return parsed_data

def open_json(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print('File ' + filename + ' not found')
        exit(-1)

    data = f.read()

    return read_json(data)

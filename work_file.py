import json
import sys

sys.path.append('../')


def write_file(filename, request):
    with open(filename, 'w') as output_file:
        output_file.write(str(request.text))


def write_file2(filename, list):
    with open(filename, 'w') as output_file:
        output_file.write(str(list) + str(","))
    """wapp_json = json.dumps(list)
    with open(filename, 'a', newline="") as file:
        file.write(wapp_json.replace("\\/", "/").encode().decode('unicode_escape'))"""


def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
        input_file.close()
    return text


def json_file(filename, mode, list):
    app_json = json.dumps(list)
    with open(filename, mode, newline="") as file:
        file.write(app_json.replace("\\/", "/").encode().decode('unicode_escape'))


def read_file_json(filename):
    with open(filename) as input_file:
        data = json.load(input_file)
        input_file.close()
    return data

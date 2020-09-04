import json


def write_file(filename, request):
    with open(filename, 'w') as output_file:
        output_file.write(str(request.text))


def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
        input_file.close()
    return text


def json_file(filename, list):
    app_json = json.dumps(list)
    with open(filename, "w", newline="") as file:
        file.write(app_json.replace("\\/", "/").encode().decode('unicode_escape'))
    file.close()


def read_file_json(filename):
    with open(filename) as input_file:
        data = json.load(input_file)
        input_file.close()
    return data



def read_text_file(ref):
    import json
    with open(ref) as json_import_data:
        data_file = json.load(json_import_data)
    return data_file


data = read_text_file('test_data.json')


def add_text_file():
    import json
    with open('test_data.json', 'w+') as add_info_file:
        json.dump(data, add_info_file)


print(data)



def read_text_file(ref):
    import json
    with open(ref) as json_import_data:
        data_file = json.load(json_import_data)
    return data_file


data_test = read_text_file('test_data.json')


def save_text_file(ref, data_file):
    import json
    with open(ref, 'w') as add_info_file:
        json.dump(data_file, add_info_file)


import random

print(f'При открытии {data_test}')
random_names = ['Миша', "Коля", "Вася", 'Илья', "Влад"]
random_specification = ['плохой', "весёлый", "красивый", "прикольный", "интересный"]
r_n = random.choice(random_names)
r_s = random.choice(random_specification)
data_test[r_n] = r_s
print(f'При закрытии {data_test}')
save_text_file('test_data.json', data_test)


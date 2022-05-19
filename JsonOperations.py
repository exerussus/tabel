

class JsonOperations:

    @staticmethod
    def read(ref):
        """Импортирует JSON в Python, и возвращает его значение.
        Аргументы: ref - ссылка на JSON, который надо присвоить переменной."""
        from json import load
        with open('data/' + ref + '.json') as json_import_data:
            data_file = load(json_import_data)
        return data_file

    @staticmethod
    def save(ref, data_file):
        """Сохраняет значение переменной в JSON.
        Аргументы: ref - ссылка на JSON, data_file - переменная,
        значение которой сохраняется в JSON."""
        from json import dump
        with open('data/' + ref + '.json', 'w') as add_info_file:
            dump(data_file, add_info_file)



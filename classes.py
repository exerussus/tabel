
class JsonOperations:

    @staticmethod
    def read(ref):
        """Импортирует JSON в Python, и возвращает его значение.
        Аргументы: ref - ссылка на JSON, который надо присвоить переменной."""
        import json
        with open('data/' + ref + '.json') as json_import_data:
            data_file = json.load(json_import_data)
        return data_file

    @staticmethod
    def save(ref, data_file):
        """Сохраняет значение переменной в JSON.
        Аргументы: ref - ссылка на JSON, data_file - переменная, значение которой сохраняется в JSON."""
        import json
        with open('data/' + ref + '.json', 'w') as add_info_file:
            json.dump(data_file, add_info_file)


class TabelInput:

    @staticmethod
    def start():
        return input("31.01, за ярцева, моисеева, 6в, 3ур, 1ч")


class TabelTextSpliter:

    @staticmethod
    def start(text):
        return text.split(', ')


class TabelSQL:

    @staticmethod
    def write():
        pass
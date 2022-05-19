class TabelInput:

    @classmethod
    def do(cls):
        return input('Вставьте данные формата "":  ')


class TabelReader:

    @classmethod
    def do(cls, name):
        from JsonOperations import JsonOperations

        return JsonOperations.read(name)


class TabelSaver:

    @classmethod
    def do(cls, name, db):
        from JsonOperations import JsonOperations

        JsonOperations.save(name, db)


class FileChecking:

    @classmethod
    def do(cls, name):
        from os.path import isdir
        return isdir(f'data/{name}.json')


class FileCreation:

    @classmethod
    def do(cls, name):
        db = ''
        TabelSaver.do(name, db)


class CheckingAndCreation:

    @classmethod
    def do(cls, name):
        if not FileChecking.do(name):
            FileCreation.do(name)


class Initialization:

    @classmethod
    def do(cls):
        CheckingAndCreation.do('teachers')
        CheckingAndCreation.do('date')


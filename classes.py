import sqlite3


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


class TabelInput:

    @staticmethod
    def start():

        """
        31.01 - date\n
        за ярцева - replaced teacher\n
        моисеева - actually teacher\n
        6в - school class\n
        3 - lesson number\n
        """

        return input("31.01, за ярцева, моисеева, 6в, 3")


class TabelTextSpliter:

    @staticmethod
    def start(text):
        return text.split(', ')


class TabelSQL:

    @staticmethod
    def db_connect():

        db = sqlite3.connect('database.db')
        return db.cursor()

    @staticmethod
    def db_teachers_creation():

        sql = TabelSQL.db_connect()
        sql.execute("""CREATE TABLE IF NOT EXISTS teachers(
        teacher_id INT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        parent_name TEXT,
        full_name TEXT,
        dative TEXT,
        genitive TEXT,
        short_native TEXT,
        short_dative TEXT
        );""")

    @staticmethod
    def db_replacing_creation():
        sql = TabelSQL.db_connect()
        sql.execute("""CREATE TABLE IF NOT EXISTS replacing(
        year INT PRIMARY KEY,
        month INT,
        day INT,
        replacing_teacher TEXT,
        actually_teacher TEXT, 
        school_class TEXT,
        lesson_number INT,
        lesson_name        
        );
        """)

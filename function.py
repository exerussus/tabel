import datetime as dt
import time
from data import *
import random


def do_title(inputting_date):
    """Создаёт титл на день"""

    now = dt.datetime.now()
    year_now = now.year
    m = inputting_date.split('.')
    try:
        day = m[0]
        month = m[1]
    except IndexError:
        month = m[0][3:]
        day = m[0][:2]
    day = int(day)
    month = int(month)
    title_day = dt.datetime(year_now, month, day)
    day_of_week = days['родительный'][title_day.strftime('%w')]
    return f'Замена на {day_of_week} ({inputting_date})'


class Timetable:

    def __init__(self, order):
        """Инициация строки типа:
            '31.01, за ярцева, моисеева, 6в, 3ур, 1ч'"""

        self.order = order

    def decypher(self):
        """Разделяет текст на отдельные элементы
        'date': date,
            'replacing_teacher' - учитель которого заменяют,
            'teacher' - заменяющий учитель,
            'index_class' - номер и буква класса,
            'index_subject' - номер урока,
            'hours' - часы,
        """
        x = self.order.split(', ')
        date = x[0]
        replacing_teacher = x[1][3:]
        teacher = x[2]
        index_class = x[3]
        index_subject = x[4][:1]
        hours = x[5][:1]
        y = {
            'date': date,
            'replacing_teacher': replacing_teacher,
            'teacher': teacher,
            'index_class': index_class,
            'index_subject': index_subject,
            'hours': hours,
        }
        return y

    def for_teacher(self):
        """За кого замена"""
        teacher = self.decypher()['replacing_teacher']
        x = 'За ' + data_teachers[teacher]['родительный'] + ':'
        return x

    def making_replace(self):
        """Создает словарь с заменами"""
        x = self.decypher()
        date = x['date']
        index_subject = x['index_subject']
        index_class = x['index_class']
        teacher = x['teacher']
        join = index_subject + ')', index_class, data_teachers[teacher]['именительный']
        join = ' '.join(join)
        try:
            data_replace[date][self.for_teacher()][index_subject] = join
        except KeyError:
            try:
                data_replace[date][self.for_teacher()] = {index_subject: join}
            except KeyError:
                data_replace[date] = {self.for_teacher(): {'1': '', '2': '', '3': '', '4': '', '5': ''}}
                data_replace[date][self.for_teacher()][index_subject] = join


def main_menu():
    # truth = random.choice(data_truth)
    # print(f'Лизонька, {truth}')
    while True:
        choice = input('   Выберите действие:\n'
                       '1. Добавить изменения\n'
                       '2. Вывести расписание\n'
                       '0. Выход\n'
                       'Ваш выбор: ')

        if choice == '1':
            while True:
                print('Для выхода нажмите 0.')
                text = input('Введите текст типа "31.01, за ярцева, моисеева, 6в, 3ур, 1ч":')
                if text == '0':
                    break
                else:
                    try:
                        n = Timetable(text)
                        n.making_replace()
                    except IndexError:
                        print("Введена некорректная информация...")
        elif choice == '2':
            date = input('Введите дату: ')

            try:
                month = date[3:]
                day = date[:2]
                int(month)
                int(day)
                print(do_title(date))
                try:
                    for a, b in data_replace[date].items():
                        print(a)
                        for i in b:
                            if b[i] != '':
                                print(b[i])
                        print('')
                except KeyError:
                    print('Нет изменений на данную дату.')
            except ValueError:
                print('Неверно введена дата...')
        elif choice == '0':
            print('Спасибо, что воспользовались программой Tabel и облегчили себе жизнь!')
            input()
            exit(0)
        else:
            print("Выберите действие из списка...")

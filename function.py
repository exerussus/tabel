import datetime as dt
import time
from data import *
from future import filter_class


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
        index_class = filter_class(x[3])
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

    def do_title(self):
        """Создаёт титл на день"""
        n = self.decypher()['date']
        now = dt.datetime.now()
        year_now = now.year
        m = n.split('.')
        day = m[0]
        month = m[1]
        if day[0] == '0':
            day = day[1:]
        if month[1] == '0':
            month = month[1:]
        day = int(day)
        month = int(month)
        title_day = dt.datetime(year_now, month, day)
        day_of_week = days['родительный'][title_day.strftime('%w')]
        return f'Замена на {day_of_week} ({n})'

    def for_teacher(self):
        """За кого замена"""
        teacher = self.decypher()['replacing_teacher']
        x = 'За ' + data_teachers[teacher]['родительный'] + ':'
        return x

    def making_replace(self):
        """Создает словарь с заменами"""
        x = self.decypher()
        self.do_title()

        join = x['index_subject'] + ')', x['index_class'], data_teachers[x['teacher']]['именительный']
        join = ' '.join(join)

        data_replace[x['date']] = x['index_subject']

        data_replace[x['date']]['for_teacher'] = self.for_teacher()
        data_replace[x['date']][x['index_subject']] = join
        return data_replace['date']['index_subject']

    def print(self):
        pass
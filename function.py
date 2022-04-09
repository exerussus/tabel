import datetime as dt
import time
from data import *


def title():
    """Создаёт титл на день"""
    now = dt.datetime.now()
    date = str(now.day) + '.' + str(now.month)
    day_of_the_week = days['2'][time.strftime('%w')]

    date = date.split('.')
    if int(date[0]) < 10:
        date[0] = '0' + date[0]
    if int(date[1]) < 10:
        date[1] = '0' + date[1]

    date = '.'.join(date)
    return f'Замена на {day_of_the_week} ({date})'


def for_teacher():
    """За кого замена"""
    teacher = 'моисеева'
    x = 'За ' + data_teachers[teacher]['родительный'] + ':'
    return x

# def create_title_of_table():
#


def decypher(inputting_text):
    """Разделяет текст на отдельные элементы
    'date': date,
        'replacing_teacher' - учитель которого заменяют,
        'teacher' - заменяющий учитель,
        'index_class' - номер и буква класса,
        'index_subject' - предмет урока,
        'hours' - часы,
    """
    x = inputting_text.split(', ')
    date = x[0]
    replacing_teacher = x[1][3:]
    teacher = x[2]
    index_class = x[3][:1]
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

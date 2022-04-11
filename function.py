import datetime as dt
import time
from data import *
from future import filter_class


def do_title(n):
    """Создаёт титл на день"""
    # if n == 0:
    #     now = dt.datetime.now()
    #     date = str(now.day) + '.' + str(now.month)
    #     day_of_the_week = days['родительный'][time.strftime('%w')]
    # else:
    #     date = n
    #     day_of_the_week = days['родительный'][time.strftime('%w')]
    m = n.split('.')
    day = m[0]
    month = m[1]
    if day[0] == '0':
       day = day[1:]
    if month[1] == '0':
       month = month[1:]
    day = int(day)
    month = int(month)
    title_day = dt.datetime(2022, month, day)
    day_of_week = days['родительный'][title_day.strftime('%w')]

    return f'Замена на {day_of_week} ({n})'


def for_teacher(y):
    """За кого замена"""
    teacher = y
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
        'index_subject' - номер урока,
        'hours' - часы,
    """
    x = inputting_text.split(', ')
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


def making_replace(y):
    """Создает словарь с заменами"""
    x = y  # decypher('31.01, за ярцеву, афонина, 6в, 2ур, 1ч')
    do_title('31.01')
    text = for_teacher(x['replacing_teacher'])
    join = x['index_subject'] + ')', x['index_class'], data_teachers[x['teacher']]['именительный']
    join = ' '.join(join)
    data_replace[x['index_subject']] = join
    print(text)
    return data_replace[x['index_subject']]

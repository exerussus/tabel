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
    teacher = 'моисеева'
    x = 'За ' + data_teachers[teacher]['родительный'] + ':'
    return x

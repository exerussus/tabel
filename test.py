
def days_generation_for_month(data_base, month):
    """Заполняет месяц днями. Всего будет 31 дней независимо от месяца.
    Аргументы: data_base - заполняемый словарь; month - заполняемый месяц в словаре."""
    str_month = str(month)
    if len(str_month) == 1:
        str_month = '0' + str_month
    for i in range(31):
        i = str(i + 1)
        if len(i) == 1:
            i = '0' + i
        data_base[month][f'{i}.' + str_month] = ''


data_base = {
    1: {}
}

month = 1

days_generation_for_month(data_base, month)

print(data_base)
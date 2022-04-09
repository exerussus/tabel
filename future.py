from data import data_classes

def filter_class(inputting_class):
    """Переводит текст в ожидаемый"""
    x = list(inputting_class)
    if len(x) > 2:
        new_x = ''
        for i in x:
            if i in data_classes:
                new_x = new_x + i
        x = new_x
        x = list(x)
        print(f'Первый срез: {x}')
    if len(x) > 2:
        for i in x:
            try:
                b = int(x[0])
            except ValueError:
                try:
                    b = int(i)
                    b = x[0]
                    x[0] = i
                    x.append(b)
                except ValueError:
                    pass

        x = ''.join(x)
        x = x[:2]
        x = list(x)
        print(f'Второй срез: {x}')
    try:
        b = int(x[0])
    except ValueError:
        b = x[0]
        x[0] = x[1]
        x[1] = b

    if x[1] == 'a' or x[1] == 'A' or x[1] == 'а' or x[1] == 'А':
        x[1] = 'А'
    if x[1] == 'b' or x[1] == 'B' or x[1] == 'в' or x[1] == 'В':
        x[1] = 'В'
    if x[1] == 'Б' or x[1] == 'б' or x[1] == 'ю' or x[1] == 'ь':
        x[1] = 'Б'
    if x[1] == 'Г' or x[1] == 'г' or x[1] == 'н' or x[1] == 'ш':
        x[1] = 'Г'
    return ''.join(x)

inputting_class = 'kaa7ad75a'

print(filter_class(inputting_class))

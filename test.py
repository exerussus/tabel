import docx
from docx.shared import Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt


month = 'февраль'
year = '2022'
doc = docx.Document()


title = doc.add_paragraph('') # Создание абзаца

title.alignment = WD_ALIGN_PARAGRAPH.CENTER  # Выравнивание по центру

title = title.add_run('Расшифровка к табелю на заработную плату\n'  # Добавление текста в абзац
          f'за {month} {year} г. (первичная) по МБОУ «Школа № 38»  г. \n'
          'Рязани\n'
          'Оплатить:\n')
title.bold = True  # Изменение стиля текста на жирный
title.font.name = 'Times New Roman'  # Изменение стиля текста на Times New Roman
title.font.size = Pt(14)  # Изменение размера текста

# добавляем таблицу 3x3
table = doc.add_table(rows = 2, cols = 7)  # rows - строки, cols - столбцы
# применяем стиль для таблицы
table.style = 'Table Grid'

# # заполняем таблицу данными
# for row in range(2):
#     for col in range(2):
#         # получаем ячейку таблицы
#         cell = table.cell(row, col)
#         # записываем в ячейку данные
#         cell.text = str(row + 1) + str(col + 1)

doc.save('example.docx')
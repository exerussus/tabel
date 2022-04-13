import docx
from docx.shared import Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt


month = 'февраль'
year = '2022'
doc = docx.Document()


title = doc.add_paragraph('')
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
title = title.add_run('Расшифровка к табелю на заработную плату\n'
          f'за {month} {year} г. (первичная) по МБОУ «Школа № 38»  г. \n'
          'Рязани\n'
          'Оплатить:\n')
title.bold = True
title.font.name = 'Times New Roman'
title.font.size = Pt(14)

# добавляем таблицу 3x3
table = doc.add_table(rows = 3, cols = 3)
# применяем стиль для таблицы
table.style = 'Table Grid'

# заполняем таблицу данными
for row in range(3):
    for col in range(3):
        # получаем ячейку таблицы
        cell = table.cell(row, col)
        # записываем в ячейку данные
        cell.text = str(row + 1) + str(col + 1)

doc.save('example.docx')
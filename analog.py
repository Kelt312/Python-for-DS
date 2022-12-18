# реализация выделения тегов из названия позиции
# print('Ура, я начал!')
# попробуем подгрузить наш прайс через pandas
import numpy as np
import pandas as pd

chint = pd.ExcelFile("chint.xlsx")  # загрузка эксель
hyu = pd.ExcelFile("hyundai.xlsx")
price_chint = chint.parse("Лист1")  # dataframe
price_hyu = hyu.parse("1")
one_v = price_chint['Описание'].values[1]  # получить значение 1

# выделение тегов
from rutermextract import TermExtractor as TE

term = TE()
for i in range(5):
    ch = term(price_chint['Описание'].values[i], strings=1)
    print(ch)

    # for i in range(5):
    hy = term(price_hyu['Полное название'].values[i], strings=1)
    print(hy)

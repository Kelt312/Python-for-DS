# реализация выделения тегов из названия позиции
# print('Ура, я начал!')
# попробуем подгрузить наш прайс через pandas
import numpy as np
import pandas as pd
from rutermextract import TermExtractor as TE
# выделение тегов

def termy(st):
    term = TE()
    return term(st, strings=1)

# сравнение по тегам

def compare_keywords(kw_1, kw_2):
    set_of_kw_1 = set([x[0] for x in kw_1])
    set_of_kw_2 = set([x[0] for x in kw_2])
    return len(set_of_kw_1 & set_of_kw_2) / min(len(set_of_kw_1), len(set_of_kw_2))

chint = pd.ExcelFile("chint.xlsx")  # загрузка эксель
hyu = pd.ExcelFile("hyundai.xlsx")
price_chint = chint.parse("Лист1")  # dataframe
price_hyu = hyu.parse("1")
#one_v = price_chint['Описание'].values[1]  # получить значение 1

kw_1 = termy(price_hyu['Полное название'].values[1]) #эталон
for k in kw_1:
    print(k)

for i in range(40,50):
    kw_2 = termy(price_hyu['Полное название'].values[i])
    print(compare_keywords(kw_1, kw_2))




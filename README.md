# Python-for-DS
Курс ПНИПУ
Итоговое задание по курсу
Цель: ценовое позиционирование оборудования различных производителей
Основные этапы реализации проекта:

1. Выделение класса и характеристик оборудования (оригинал задан заранее).

Дано наименование оборудования, содержащие некоторое функциональное описание и технические характеристики.
Задача: вычленить функционал и ключевые технические характеристики оборудования, подобрать аналоги от заданных производителей.
Например, дано:  Воздушный авт. выкл. выкатной 3P 2500А 80кА расцепитель Н ВА-732
Функционал – автоматический выключатель
Тип – Воздушный
Исполнение – выкатной
Кол-во полюсов – 3
Номинальный ток  - 2500А
ПКС – 80кА
Тип расцепителя – H
Серия – ВА-732

2. Поиск в данном классе аналога (другой производитель) с подобными тех характеристиками

Обработка прайсов в формате xml, поиск совпадений по кол-ву заданных параметров.
Выгрузка данных в таблицу с сортировкой по стоимости оборудования.
Например, один из аналогов: Воздушный авт. выкл. NA8G-2500-2500H/3P выдвиж., 2500A, 80kA, тип H, AC220В (R)

3. Создание приложения с интерактивным интерфейсом в котором возможны: 

настройка поиска (не все характеристики могут быть важны)
вызов из exel (выделение ячейки с нужным оборудованием -> передача информации в программу
задание пути для сохранения файла данных
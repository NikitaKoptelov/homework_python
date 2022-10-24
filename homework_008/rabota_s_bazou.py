from optparse import Values
import sqlite3
import os
from unicodedata import name
 

con = ''
index_tab = 0
index_str_tab = 0
name_tablet = ''
name_stolb = ''
con = sqlite3.connect('D:/lesson_Python/homework_python/homework_008/baza_magazin.db')

def init():
    global con
    global index_tab
    global index_str_tab
    global name_tablet
    global name_stolb

 
def sql_fetch_name_table(con):                              #  вызов всех названий таблиц в базе данных
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    name_tables = [list(row) for row in cursorObj.fetchall()]
    # return name_tables
    print(name_tables)
sql_fetch_name_table(con)

def sql_fetch(con):               #   вызов каждой таблици по имени
    Values = ('Категории')
    cursorObj = con.cursor()
    cursorObj.execute(f'SELECT * from {Values}')
    rows=cursorObj.fetchall()
    res=[list(row) for row in rows]
    
    return res
    # for row in rows:
    #     return res.append(row)
    # print(res)
# sql_fetch(con)

# def sql_fetch(con, name_tablet, name_stolb):               #   вызов каждой таблици по имени с выводом только названного столбца
#     cursorObj = con.cursor()
#     cursorObj.execute(f'select {name_stolb} from {name_tablet}')
#     rows=cursorObj.fetchall()
#     for row in rows:
#         print(row)
# sql_fetch(con, 'Товары', 'Наименование_товара')

# def sql_fetch(con, name_tablet, name_stolb, index):               #   вызов каждой таблици по имени с выводом только названного столбца в один массив и парсинг для получения одного значения
#     cursorObj = con.cursor()
#     cursorObj.execute(f'select {name_stolb} from {name_tablet}')
#     # row=cursorObj.fetchall()
#     stroka_stolbca=[row for row in cursorObj.fetchall()]
#     print(stroka_stolbca[index][0])
# sql_fetch(con, 'Товары', 'Наименование_товара', 4)


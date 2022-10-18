import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Подключение к базе данных SQLite прошло успешно")
    except Error as e:
        print(f"Произошла ошибка '{e}'")
    return connection



create_connection('/media/nik/Disk_2/lesson_Python/homework_python/homework_008/dannie_oranizacii.db')


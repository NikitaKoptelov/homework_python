from PyQt6 import QtWidgets, uic
import sys
 
app = QtWidgets.QApplication([])
win = uic.loadUi("D:/lesson_Python/homework_python/homework_008/untitled.py") # расположение вашего файла .ui
 
win.show()
sys.exit(app.exec())
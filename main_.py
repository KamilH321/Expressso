import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('cof.ui', self)
        self.pushButton.clicked.connect(self.ar)
        self.pushButton_2.clicked.connect(self.li)
        self.pushButton_3.clicked.connect(self.rob)

    def ar(self):
        c = 'Арабика'
        con = sqlite3.connect('cofee.db')
        cur = con.cursor()
        result = cur.execute(f"SELECT * FROM coffe_information WHERE сорт == '{c}'").fetchall()
        s = []
        for i in result:
            for j in i:
                s.append(j)
        self.label_2.setText(f'Сорт:{s[1]} Степень обжарки:{s[2]} Тип:{s[3]} \nВкус:{s[4]} \nЦена:{s[5]} р. \nОбъем упаковки:{s[6]}')

    def li(self):
        c = 'Либерика'
        con = sqlite3.connect('cofee.db')
        cur = con.cursor()
        result = cur.execute(f"SELECT * FROM coffe_information WHERE сорт == '{c}'").fetchall()
        s = []
        for i in result:
            for j in i:
                s.append(j)
        self.label_2.setText(
            f'Сорт:{s[1]} Степень обжарки:{s[2]} Тип:{s[3]} \nВкус:{s[4]} \nЦена:{s[5]} р. \nОбъем упаковки:{s[6]}')

    def rob(self):
        c = 'Робуста'
        con = sqlite3.connect('cofee.db')
        cur = con.cursor()
        result = cur.execute(f"SELECT * FROM coffe_information WHERE сорт == '{c}'").fetchall()
        s = []
        for i in result:
            for j in i:
                s.append(j)
        self.label_2.setText(
            f'Сорт:{s[1]} Степень обжарки:{s[2]} Тип:{s[3]} \nВкус:{s[4]} \nЦена:{s[5]} р. \nОбъем упаковки:{s[6]}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
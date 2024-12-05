import io
import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtWidgets import QLabel, QHeaderView

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>785</width>
    <height>533</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>371</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>36</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Кофе</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>100</y>
      <width>751</width>
      <height>371</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>785</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setFixedSize(self.size())
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        req = """SELECT ID, название_сорта, молотый__в_зернах, описание_вкуса, цена, объем_упаковки from coffee_specs"""
        self.result = cur.execute(req).fetchall()
        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зёрнах', 'описание вкуса', 'цена', 'объем упаковки'])
        for i, x in enumerate(self.result):
            for j, y in enumerate(x):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(y)))
        for v in range(self.tableWidget.columnCount()):
            self.tableWidget.horizontalHeader().setSectionResizeMode(v, QHeaderView.ResizeMode.Stretch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
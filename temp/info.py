# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_help.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_helpWindow(object):
    def setupUi(self, helpWindow):
        helpWindow.setObjectName("helpWindow")
        helpWindow.resize(700, 314)
        helpWindow.setStyleSheet("color: black;\n"
"    font-family: ;\n"
"font: 11pt \"Noto Serif CJK JP\";\n"
"background-color: rgba(255, 255, 255, 85);")
        self.centralwidget = QtWidgets.QWidget(helpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setStyleSheet("color: black;\n"
"    font-family: \'Roboto Slab\', serif;")
        self.textBrowser.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        helpWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(helpWindow)
        self.statusbar.setObjectName("statusbar")
        helpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(helpWindow)
        QtCore.QMetaObject.connectSlotsByName(helpWindow)

    def retranslateUi(self, helpWindow):
        _translate = QtCore.QCoreApplication.translate
        helpWindow.setWindowTitle(_translate("helpWindow", "о программе"))
        self.textBrowser.setHtml(_translate("helpWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Slab,serif\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Автор: </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Дата обновления: 28.04.2019</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Версия 1.0.0</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Список изменений версии 1.0.0:</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1) Добавлена анимация всех кнопок,</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2) Исправлена ошибка в определении седловой точки,</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3) Некоторые косметические изменения,</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4) добавлены новые иконки к кнопкам,</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5) В основное окно добавлено &quot;<span style=\" font-style:italic;\">action&quot;</span>  меню,</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6) Удаелены ненужные элементы.</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))



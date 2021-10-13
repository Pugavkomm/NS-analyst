# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_plot_window(object):
    def setupUi(self, plot_window):
        plot_window.setObjectName("plot_window")
        plot_window.resize(956, 602)
        plot_window.setStyleSheet("color: black;\n"
"    font-family: ;\n"
"font: 11pt \"Noto Serif CJK JP\";\n"
"background-color: rgba(255, 255, 255, 85);")
        self.centralwidget = QtWidgets.QWidget(plot_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearButton.setStyleSheet("float: flat;\n"
"margin-rigth: 3%;\n"
"    margin-top: 5px;\n"
"    \n"
" border: 1px rgba(114, 147, 182, 1);\n"
"    padding: 5px 9px;\n"
"    font-size: 1.2em;\n"
"    background-color: rgba(114, 147, 182, 1);\n"
"    text-shadow: #454545 0 0 2px;\n"
"    border-bottom: 4px solid rgba(114, 147, 182, 1);\n"
"    color: white;\n"
"    font-family: \'Roboto Slab\', serif;\n"
"\n"
"")
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 3, 0, 1, 1)
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setObjectName("MplWidget")
        self.gridLayout.addWidget(self.MplWidget, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        plot_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(plot_window)
        self.statusbar.setObjectName("statusbar")
        plot_window.setStatusBar(self.statusbar)

        self.retranslateUi(plot_window)
        QtCore.QMetaObject.connectSlotsByName(plot_window)

    def retranslateUi(self, plot_window):
        _translate = QtCore.QCoreApplication.translate
        plot_window.setWindowTitle(_translate("plot_window", "график"))
        self.clearButton.setText(_translate("plot_window", "вернуть параметры и очистить данные"))


from mplwidget import MplWidget

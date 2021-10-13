# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_plot.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings_plot_window(object):
    def setupUi(self, settings_plot_window):
        settings_plot_window.setObjectName("settings_plot_window")
        settings_plot_window.setWindowModality(QtCore.Qt.NonModal)
        settings_plot_window.setEnabled(True)
        settings_plot_window.resize(276, 574)
        settings_plot_window.setMinimumSize(QtCore.QSize(276, 574))
        settings_plot_window.setMaximumSize(QtCore.QSize(276, 574))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        settings_plot_window.setPalette(palette)
        settings_plot_window.setStyleSheet("color: black;\n"
"    font-family: ;\n"
"font: 11pt \"Noto Serif CJK JP\";\n"
"background-color: rgba(255, 255, 255, 85);")
        settings_plot_window.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.centralwidget = QtWidgets.QWidget(settings_plot_window)
        self.centralwidget.setObjectName("centralwidget")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(150, 500, 111, 41))
        self.okButton.setStyleSheet("QPushButton {\n"
"float: right;\n"
"margin-rigth: 3%;\n"
"    margin-top: 5px;\n"
"    background-shadow: 1px;\n"
" border: 1px rgba(114, 147, 182, 1);\n"
"    padding: 5px 9px;\n"
"    font-size: 1.2em;\n"
"    background-color: rgba(114, 147, 182, 1);\n"
"    text-shadow: #454545 0 0 3px;\n"
"    border-bottom: 4px solid rgba(114, 147, 182, 1);\n"
"    color: white;\n"
"    font-family: ;\n"
"font: 11pt \"Noto Serif CJK JP\";\n"
"\n"
"\n"
"  border: 1px solid rgba(114, 147, 182, 1);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(163, 175, 188);\n"
"}\n"
"")
        self.okButton.setObjectName("okButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 252, 474))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.xmin = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.xmin.setStyleSheet("float: flat;\n"
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
        self.xmin.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.xmin.setProperty("showGroupSeparator", False)
        self.xmin.setDecimals(10)
        self.xmin.setMinimum(-99999.0)
        self.xmin.setMaximum(99999.99)
        self.xmin.setObjectName("xmin")
        self.horizontalLayout.addWidget(self.xmin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.xmax = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.xmax.setStyleSheet("float: flat;\n"
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
        self.xmax.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.xmax.setProperty("showGroupSeparator", False)
        self.xmax.setDecimals(10)
        self.xmax.setMinimum(-99999.0)
        self.xmax.setMaximum(99999.99)
        self.xmax.setObjectName("xmax")
        self.horizontalLayout_2.addWidget(self.xmax)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.ymin = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.ymin.setStyleSheet("float: flat;\n"
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
        self.ymin.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.ymin.setProperty("showGroupSeparator", False)
        self.ymin.setDecimals(10)
        self.ymin.setMinimum(-99999.0)
        self.ymin.setMaximum(99999.99)
        self.ymin.setObjectName("ymin")
        self.horizontalLayout_3.addWidget(self.ymin)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.ymax = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.ymax.setStyleSheet("float: flat;\n"
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
        self.ymax.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.ymax.setProperty("showGroupSeparator", False)
        self.ymax.setDecimals(10)
        self.ymax.setMinimum(-99999.0)
        self.ymax.setMaximum(99999.99)
        self.ymax.setObjectName("ymax")
        self.horizontalLayout_4.addWidget(self.ymax)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setStyleSheet("float: flat;\n"
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
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(4, "")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.colorlineCombobox = QtWidgets.QComboBox(self.layoutWidget)
        self.colorlineCombobox.setStyleSheet("float: flat;\n"
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
        self.colorlineCombobox.setObjectName("colorlineCombobox")
        self.colorlineCombobox.addItem("")
        self.colorlineCombobox.addItem("")
        self.colorlineCombobox.addItem("")
        self.colorlineCombobox.addItem("")
        self.colorlineCombobox.addItem("")
        self.colorlineCombobox.setItemText(4, "")
        self.horizontalLayout_6.addWidget(self.colorlineCombobox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.sizepoints = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.sizepoints.setStyleSheet("float: flat;\n"
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
        self.sizepoints.setDecimals(2)
        self.sizepoints.setMinimum(0.01)
        self.sizepoints.setSingleStep(0.1)
        self.sizepoints.setProperty("value", 0.01)
        self.sizepoints.setObjectName("sizepoints")
        self.horizontalLayout_7.addWidget(self.sizepoints)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setStyleSheet("float: flat;\n"
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
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.linetopoint = QtWidgets.QCheckBox(self.layoutWidget)
        self.linetopoint.setStyleSheet("float: flat;\n"
"margin-rigth: 3%;\n"
"    margin-top: 5px;\n"
"    \n"
" border: 1px rgba(114, 147, 182, 1);\n"
"    padding: 5px 9px;\n"
"    font-size: .2em;\n"
"    background-color: rgba(114, 147, 182, 1);\n"
"    text-shadow: #454545 0 0 2px;\n"
"    border-bottom: 4px solid rgba(114, 147, 182, 1);\n"
"    color: white;\n"
"    font-family: \'Roboto Slab\', serif;\n"
"\n"
"")
        self.linetopoint.setObjectName("linetopoint")
        self.verticalLayout.addWidget(self.linetopoint)
        self.hidepoint = QtWidgets.QCheckBox(self.layoutWidget)
        self.hidepoint.setStyleSheet("float: flat;\n"
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
        self.hidepoint.setObjectName("hidepoint")
        self.verticalLayout.addWidget(self.hidepoint)
        settings_plot_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(settings_plot_window)
        self.statusbar.setObjectName("statusbar")
        settings_plot_window.setStatusBar(self.statusbar)

        self.retranslateUi(settings_plot_window)
        QtCore.QMetaObject.connectSlotsByName(settings_plot_window)

    def retranslateUi(self, settings_plot_window):
        _translate = QtCore.QCoreApplication.translate
        settings_plot_window.setWindowTitle(_translate("settings_plot_window", "Параметры графика"))
        self.okButton.setText(_translate("settings_plot_window", "применить"))
        self.label.setText(_translate("settings_plot_window", "<html><head/><body><p align=\"right\">xmin</p></body></html>"))
        self.label_2.setText(_translate("settings_plot_window", "<html><head/><body><p align=\"right\">xmax</p></body></html>"))
        self.label_3.setText(_translate("settings_plot_window", "<html><head/><body><p align=\"right\">ymin</p></body></html>"))
        self.label_4.setText(_translate("settings_plot_window", "<html><head/><body><p align=\"right\">ymax</p></body></html>"))
        self.label_5.setText(_translate("settings_plot_window", "цвет точек"))
        self.comboBox.setItemText(0, _translate("settings_plot_window", "черный"))
        self.comboBox.setItemText(1, _translate("settings_plot_window", "красный"))
        self.comboBox.setItemText(2, _translate("settings_plot_window", "зеленый"))
        self.comboBox.setItemText(3, _translate("settings_plot_window", "синий"))
        self.label_7.setText(_translate("settings_plot_window", "цвет линии"))
        self.colorlineCombobox.setItemText(0, _translate("settings_plot_window", "черный"))
        self.colorlineCombobox.setItemText(1, _translate("settings_plot_window", "красный"))
        self.colorlineCombobox.setItemText(2, _translate("settings_plot_window", "зеленый"))
        self.colorlineCombobox.setItemText(3, _translate("settings_plot_window", "синий"))
        self.label_6.setText(_translate("settings_plot_window", "размер точек"))
        self.checkBox.setText(_translate("settings_plot_window", "сетка графика"))
        self.linetopoint.setText(_translate("settings_plot_window", "соединять точки"))
        self.hidepoint.setText(_translate("settings_plot_window", "скрывать точки "))



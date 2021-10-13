# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1337, 655)
        MainWindow.setMinimumSize(QtCore.QSize(1337, 655))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/scatter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: black;\n"
"    font-family: ;\n"
"font: 11pt \"Noto Serif CJK JP\";\n"
"background-color: rgba(255, 255, 255, 85);")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(1, -1, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_6.addWidget(self.line_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.display_system = QtWidgets.QTextBrowser(self.centralwidget)
        self.display_system.setAutoFillBackground(True)
        self.display_system.setStyleSheet("color: black;\n"
"font-family: ;\n"
"font: 11pt \"Noto Serif CJK JP\";")
        self.display_system.setFrameShape(QtWidgets.QFrame.Box)
        self.display_system.setFrameShadow(QtWidgets.QFrame.Plain)
        self.display_system.setLineWidth(1)
        self.display_system.setMidLineWidth(1)
        self.display_system.setTabChangesFocus(True)
        self.display_system.setObjectName("display_system")
        self.verticalLayout_6.addWidget(self.display_system)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.plotBotton = QtWidgets.QPushButton(self.centralwidget)
        self.plotBotton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plotBotton.setMouseTracking(True)
        self.plotBotton.setAutoFillBackground(False)
        self.plotBotton.setStyleSheet("QPushButton {\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/icon_app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plotBotton.setIcon(icon1)
        self.plotBotton.setCheckable(False)
        self.plotBotton.setChecked(False)
        self.plotBotton.setAutoRepeat(False)
        self.plotBotton.setAutoExclusive(False)
        self.plotBotton.setDefault(True)
        self.plotBotton.setFlat(False)
        self.plotBotton.setObjectName("plotBotton")
        self.horizontalLayout_8.addWidget(self.plotBotton)
        self.pushplotsystem = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushplotsystem.sizePolicy().hasHeightForWidth())
        self.pushplotsystem.setSizePolicy(sizePolicy)
        self.pushplotsystem.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushplotsystem.setMouseTracking(True)
        self.pushplotsystem.setAutoFillBackground(False)
        self.pushplotsystem.setStyleSheet("QPushButton {\n"
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
        self.pushplotsystem.setCheckable(False)
        self.pushplotsystem.setChecked(False)
        self.pushplotsystem.setAutoRepeat(False)
        self.pushplotsystem.setAutoExclusive(False)
        self.pushplotsystem.setDefault(True)
        self.pushplotsystem.setFlat(False)
        self.pushplotsystem.setObjectName("pushplotsystem")
        self.horizontalLayout_8.addWidget(self.pushplotsystem)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_8.addWidget(self.line)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.findfixedButton = QtWidgets.QPushButton(self.centralwidget)
        self.findfixedButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.findfixedButton.setMouseTracking(True)
        self.findfixedButton.setAutoFillBackground(False)
        self.findfixedButton.setStyleSheet("QPushButton {\n"
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
        self.findfixedButton.setCheckable(False)
        self.findfixedButton.setChecked(False)
        self.findfixedButton.setAutoRepeat(False)
        self.findfixedButton.setAutoExclusive(False)
        self.findfixedButton.setDefault(True)
        self.findfixedButton.setFlat(False)
        self.findfixedButton.setObjectName("findfixedButton")
        self.horizontalLayout_11.addWidget(self.findfixedButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.text_fixed = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_fixed.setAutoFillBackground(True)
        self.text_fixed.setStyleSheet("color: black;\n"
"font-family: ;\n"
"font: 11pt \"Noto Serif CJK JP\";")
        self.text_fixed.setFrameShape(QtWidgets.QFrame.Box)
        self.text_fixed.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_fixed.setLineWidth(1)
        self.text_fixed.setMidLineWidth(1)
        self.text_fixed.setTabChangesFocus(True)
        self.text_fixed.setObjectName("text_fixed")
        self.verticalLayout_8.addWidget(self.text_fixed)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_8.addWidget(self.line_5)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.findmultButton = QtWidgets.QPushButton(self.centralwidget)
        self.findmultButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.findmultButton.setMouseTracking(True)
        self.findmultButton.setAutoFillBackground(False)
        self.findmultButton.setStyleSheet("QPushButton {\n"
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
        self.findmultButton.setCheckable(False)
        self.findmultButton.setChecked(False)
        self.findmultButton.setAutoRepeat(False)
        self.findmultButton.setAutoExclusive(False)
        self.findmultButton.setDefault(True)
        self.findmultButton.setFlat(False)
        self.findmultButton.setObjectName("findmultButton")
        self.horizontalLayout_12.addWidget(self.findmultButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.text_mult = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_mult.setAutoFillBackground(True)
        self.text_mult.setStyleSheet("color: black;\n"
"font-family: ;\n"
"font: 11pt \"Noto Serif CJK JP\";")
        self.text_mult.setFrameShape(QtWidgets.QFrame.Box)
        self.text_mult.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_mult.setLineWidth(1)
        self.text_mult.setMidLineWidth(1)
        self.text_mult.setTabChangesFocus(True)
        self.text_mult.setObjectName("text_mult")
        self.verticalLayout_8.addWidget(self.text_mult)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_8.addWidget(self.line_4)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.koefButton = QtWidgets.QPushButton(self.centralwidget)
        self.koefButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.koefButton.setMouseTracking(True)
        self.koefButton.setAutoFillBackground(False)
        self.koefButton.setStyleSheet("QPushButton {\n"
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
        self.koefButton.setCheckable(False)
        self.koefButton.setChecked(False)
        self.koefButton.setAutoRepeat(False)
        self.koefButton.setAutoExclusive(False)
        self.koefButton.setDefault(True)
        self.koefButton.setFlat(False)
        self.koefButton.setObjectName("koefButton")
        self.horizontalLayout_13.addWidget(self.koefButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.text_koef_sadle = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_koef_sadle.setAutoFillBackground(True)
        self.text_koef_sadle.setStyleSheet("color: black;\n"
"font-family: ;\n"
"font: 11pt \"Noto Serif CJK JP\";")
        self.text_koef_sadle.setFrameShape(QtWidgets.QFrame.Box)
        self.text_koef_sadle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_koef_sadle.setLineWidth(1)
        self.text_koef_sadle.setMidLineWidth(1)
        self.text_koef_sadle.setTabChangesFocus(True)
        self.text_koef_sadle.setObjectName("text_koef_sadle")
        self.verticalLayout_8.addWidget(self.text_koef_sadle)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_8.addWidget(self.line_6)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.clearallBottom = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearallBottom.sizePolicy().hasHeightForWidth())
        self.clearallBottom.setSizePolicy(sizePolicy)
        self.clearallBottom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearallBottom.setMouseTracking(True)
        self.clearallBottom.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clearallBottom.setAutoFillBackground(False)
        self.clearallBottom.setStyleSheet("QPushButton {\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearallBottom.setIcon(icon2)
        self.clearallBottom.setCheckable(False)
        self.clearallBottom.setChecked(False)
        self.clearallBottom.setAutoRepeat(False)
        self.clearallBottom.setAutoExclusive(False)
        self.clearallBottom.setAutoDefault(False)
        self.clearallBottom.setDefault(True)
        self.clearallBottom.setFlat(False)
        self.clearallBottom.setObjectName("clearallBottom")
        self.horizontalLayout_14.addWidget(self.clearallBottom)
        self.verticalLayout_8.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_7.addWidget(self.line_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1337, 28))
        self.menubar.setStyleSheet("background-color:  rgba(114, 147, 182, 1);\n"
"selection-background-color: rgb(163, 175, 188);\n"
"")
        self.menubar.setObjectName("menubar")
        self.File = QtWidgets.QMenu(self.menubar)
        self.File.setObjectName("File")
        self.menu = QtWidgets.QMenu(self.File)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.exit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon3)
        self.exit.setObjectName("exit")
        self.infoMenu = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoMenu.setIcon(icon4)
        self.infoMenu.setObjectName("infoMenu")
        self.settIngIntMenu = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settIngIntMenu.setIcon(icon5)
        self.settIngIntMenu.setObjectName("settIngIntMenu")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.saveas = QtWidgets.QAction(MainWindow)
        self.saveas.setObjectName("saveas")
        self.selectBottom = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectBottom.setIcon(icon6)
        self.selectBottom.setObjectName("selectBottom")
        self.setplotMenu = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/box-plot-graphic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setplotMenu.setIcon(icon7)
        self.setplotMenu.setObjectName("setplotMenu")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.input_system = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/input_system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.input_system.setIcon(icon8)
        self.input_system.setIconVisibleInMenu(True)
        self.input_system.setObjectName("input_system")
        self.menu.addAction(self.action)
        self.menu.addAction(self.saveas)
        self.File.addSeparator()
        self.File.addAction(self.input_system)
        self.File.addAction(self.menu.menuAction())
        self.File.addAction(self.selectBottom)
        self.File.addAction(self.exit)
        self.File.addSeparator()
        self.menu_2.addAction(self.settIngIntMenu)
        self.menu_2.addAction(self.setplotMenu)
        self.menu_3.addAction(self.infoMenu)
        self.menu_3.addAction(self.action_4)
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.toolBar.addAction(self.input_system)
        self.toolBar.addAction(self.selectBottom)
        self.toolBar.addAction(self.settIngIntMenu)
        self.toolBar.addAction(self.setplotMenu)
        self.toolBar.addAction(self.exit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.display_system, self.plotBotton)
        MainWindow.setTabOrder(self.plotBotton, self.pushplotsystem)
        MainWindow.setTabOrder(self.pushplotsystem, self.text_fixed)
        MainWindow.setTabOrder(self.text_fixed, self.findmultButton)
        MainWindow.setTabOrder(self.findmultButton, self.text_mult)
        MainWindow.setTabOrder(self.text_mult, self.koefButton)
        MainWindow.setTabOrder(self.koefButton, self.text_koef_sadle)
        MainWindow.setTabOrder(self.text_koef_sadle, self.clearallBottom)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Построитель"))
        self.display_system.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Serif CJK JP\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\';\">Правые части вводятся в следующем виде:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\';\">.3 * x * y + w_p * x ** 2 * sin(2 * pi * w_p)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\';\">\'**\' - степень</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\';\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\';\"><br /></p></body></html>"))
        self.plotBotton.setText(_translate("MainWindow", "построение отображения"))
        self.pushplotsystem.setText(_translate("MainWindow", "построение системы"))
        self.findfixedButton.setText(_translate("MainWindow", "найти неподвижную точку"))
        self.text_fixed.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Serif CJK JP\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.findmultButton.setText(_translate("MainWindow", "найти мультипликаторы"))
        self.koefButton.setText(_translate("MainWindow", "коэффициенты к сепаратрисам"))
        self.clearallBottom.setText(_translate("MainWindow", "очистить все"))
        self.File.setTitle(_translate("MainWindow", "файл"))
        self.menu.setTitle(_translate("MainWindow", "сохранить"))
        self.menu_2.setTitle(_translate("MainWindow", "параметры"))
        self.menu_3.setTitle(_translate("MainWindow", "информация"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.exit.setText(_translate("MainWindow", "выход"))
        self.exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.infoMenu.setText(_translate("MainWindow", "о программе"))
        self.settIngIntMenu.setText(_translate("MainWindow", "параметры интегрирования"))
        self.settIngIntMenu.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.action.setText(_translate("MainWindow", "сохранить"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.saveas.setText(_translate("MainWindow", "сохранить как..."))
        self.saveas.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.selectBottom.setText(_translate("MainWindow", "выбрать систему"))
        self.setplotMenu.setText(_translate("MainWindow", "параметры графика"))
        self.setplotMenu.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_4.setText(_translate("MainWindow", "метод интегрирования"))
        self.input_system.setText(_translate("MainWindow", "задать систему"))



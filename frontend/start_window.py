# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_templates/start_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NS_startup(object):
    def setupUi(self, NS_startup):
        NS_startup.setObjectName("NS_startup")
        NS_startup.resize(362, 325)
        self.twoDsystem = QtWidgets.QPushButton(NS_startup)
        self.twoDsystem.setGeometry(QtCore.QRect(20, 60, 161, 81))
        self.twoDsystem.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.twoDsystem.setObjectName("twoDsystem")
        self.threeDsystem = QtWidgets.QPushButton(NS_startup)
        self.threeDsystem.setGeometry(QtCore.QRect(180, 60, 161, 81))
        self.threeDsystem.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.threeDsystem.setObjectName("threeDsystem")
        self.NDsystem = QtWidgets.QPushButton(NS_startup)
        self.NDsystem.setGeometry(QtCore.QRect(100, 140, 161, 81))
        self.NDsystem.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.NDsystem.setObjectName("NDsystem")
        self.label = QtWidgets.QLabel(NS_startup)
        self.label.setGeometry(QtCore.QRect(0, 300, 361, 22))
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")

        self.retranslateUi(NS_startup)
        QtCore.QMetaObject.connectSlotsByName(NS_startup)

    def retranslateUi(self, NS_startup):
        _translate = QtCore.QCoreApplication.translate
        NS_startup.setWindowTitle(_translate("NS_startup", "NS-analyst"))
        self.twoDsystem.setText(_translate("NS_startup", "2D system"))
        self.threeDsystem.setText(_translate("NS_startup", "3D system"))
        self.NDsystem.setText(_translate("NS_startup", "ND system"))
        self.label.setText(_translate("NS_startup", "Version 0.0.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NS_startup = QtWidgets.QDialog()
    ui = Ui_NS_startup()
    ui.setupUi(NS_startup)
    NS_startup.show()
    sys.exit(app.exec_())

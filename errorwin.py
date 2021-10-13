# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_errorwin(object):
    def setupUi(self, errorwin):
        errorwin.setObjectName("errorwin")
        errorwin.resize(248, 164)
        self.centralwidget = QtWidgets.QWidget(errorwin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.text_error = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_error.setObjectName("text_error")
        self.gridLayout.addWidget(self.text_error, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        errorwin.setCentralWidget(self.centralwidget)

        self.retranslateUi(errorwin)
        QtCore.QMetaObject.connectSlotsByName(errorwin)

    def retranslateUi(self, errorwin):
        _translate = QtCore.QCoreApplication.translate
        errorwin.setWindowTitle(_translate("errorwin", "ошибка"))
        self.text_error.setHtml(_translate("errorwin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("errorwin", "ok"))



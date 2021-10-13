#version 0.0.1 alpha
import sys  # sys нужен для передачи argv в QApplication
import time
import os
import matplotlib
import Map_wd
import plotuiwin
import info
import integwin
import findfixedwin
import setting_plotwin
import input_systemwin
from PyQt5 import QtWidgets
import design
import info
import wid_info
import Map_wd
import info_dialog
#from plyer import notification
from PyQt5.QtWidgets import QInputDialog, qApp
import threading
from multiprocessing import Process
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
import errorwin
from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt


import numpy as np


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow, info.Ui_helpWindow,
                 integwin.Ui_integrWin, input_systemwin.Ui_inpusystemWin, setting_plotwin.Ui_settings_plot_window,
                 findfixedwin.Ui_findmultWin, plotuiwin.Ui_plot_window, errorwin.Ui_errorwin):
    def __init__(self):

        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.textinfo = 'тестовый текст в информации\n\
            о программе'
        self.indicator_input_system = 0

        # self.setupUi_info()
        self.initUI()
        self.textx = ''
        self.texty = ''
        self.wp = 0.0
        self.h = 0.01
        self.n = 10000
        self.x_fixed = []
        self.y_fixed = []
        self.period_fixed = []
        self.sadle_number = []
        self.k_sadle1 = []
        self.k_sadle2 = []
        self.period_warning = 0
        self.mult = []
        self.x_lim_min = -10
        self.x_lim_max = 10
        self.y_lim_min = -10
        self.y_lim_max = 10
        self.toolbar = 0
        self.__x0 = 0
        self.__y0 = 0
        self.gridbool = True
        self.point_size_var = 1
        self.color_points = 'black'
        self.linetopoint = False
        self.hidepoints = False
        self.linecolormap = 'black'

    def initUI(self):

        self.setupUi(self)
        self.plotBotton.setStatusTip('открыть окно графика')
        self.exit.setStatusTip('выход из программы')
        self.selectBottom.setStatusTip('выбрать систему из сохраненных')
        self.settIngIntMenu.setStatusTip(
            'шаг интегрирования и количество итераций')
        self.clearallBottom.setStatusTip(
            'удалить найденные неподвижные точки и их мультипликаторы')
        self.findfixedButton.setStatusTip(
            'найти неподвижную точку из приближения')
        self.findmultButton.setStatusTip(
            'найти мультипликаторы неподвижных точек')
        self.setplotMenu.setStatusTip('настройка окна графика')
        self.koefButton.setStatusTip('отобразить, если есть')
        self.pushplotsystem.setStatusTip('открыть окно графика')
        self.input_system.setStatusTip('ввести систему с клавиатуры')
        #self.inputBotton.clicked.connect(self.open_input_system)
        # self.plotBotton.clicked.connect(self.multiP)
        self.plotBotton.clicked.connect(self.display_plot)
        self.findfixedButton.clicked.connect(self.display_find_fixed)
        self.findmultButton.clicked.connect(self.find_mult_method)
        self.clearallBottom.clicked.connect(self.clear_all)
        self.koefButton.clicked.connect(self.display_sadle_koef)
        self.pushplotsystem.clicked.connect(self.display_plot_system)

        self.input_system.triggered.connect(self.open_input_system)
        self.infoMenu.triggered.connect(self.open_info_program)
        self.setplotMenu.triggered.connect(self.display_plot_set)
        self.exit.triggered.connect(qApp.quit)
        # self.settIngIntMenu.triggered.connect(self.input_settings_integrate)
        self.settIngIntMenu.triggered.connect(self.open_setting_integrate)
        menubar = self.menuBar()

    def display_plot(self):
        if self.indicator_input_system == 0:
            texterror = 'необходимо ввести систему'
            self.showDialogerror(texterror)
        else:
            self.windowplot = QtWidgets.QMainWindow()
            self.uiplot = plotuiwin.Ui_plot_window()
            self.uiplot.setupUi(self.windowplot)
            self.toolbarmap = NavigationToolbar(
                self.uiplot.MplWidget.canvas, self)
            self.toolbarmap.setStyleSheet("float: flat;\n"
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
            self.windowplot.addToolBar(self.toolbarmap)

            #plt.xlim([self.x_lim_min, self.x_lim_max])
            # self.ui.MplWidget.canvas.axes.clear()
            self.uiplot.MplWidget.canvas.axes.set_xlim(
                [self.x_lim_min, self.x_lim_max])
            self.uiplot.MplWidget.canvas.axes.set_ylim(
                [self.y_lim_min, self.y_lim_max])
            self.uiplot.MplWidget.canvas.axes.grid(self.gridbool)
            self.uiplot.MplWidget.canvas.mpl_connect(
                'button_press_event', self.onclick_plot_initial)
            # self.uiplot.clearButton.clicked.connect(self.uiplot.MplWidget.canvas.axes.clear)
            self.uiplot.clearButton.clicked.connect(self.display_plot)

            self.windowplot.show()

    def onclick_plot_initial(self, event):
        if self.toolbarmap.mode == '':
            #self.__x0 = event.xdata
            #self.__y0 = event.ydata
            self.model.get_initial(event.xdata, event.ydata)
            xnew, ynew, vx_p, vy_p = self.model.rk4()
            if (self.linetopoint == True and self.hidepoints == False):
                self.uiplot.MplWidget.canvas.axes.scatter(
                    vx_p, vy_p, color=self.color_points, s=self.point_size_var)
                self.uiplot.MplWidget.canvas.axes.plot(
                    vx_p, vy_p, color=self.linecolormap)
            if (self.linetopoint == True and self.hidepoints == True):
                self.uiplot.MplWidget.canvas.axes.plot(
                    vx_p, vy_p, color=self.linecolormap)
            if (self.linetopoint == False and self.hidepoints == False):
                self.uiplot.MplWidget.canvas.axes.scatter(
                    vx_p, vy_p, color=self.color_points, s=self.point_size_var)
            if (self.linetopoint == False and self.hidepoints == True):
                None
            self.uiplot.MplWidget.canvas.draw()

    def display_plot_system(self):
        if self.indicator_input_system == 0:
            texterror = 'необходимо ввести систему'
            self.showDialogerror(texterror)
        else:
            self.windowplotsystem = QtWidgets.QMainWindow()
            self.uiplotsystem = plotuiwin.Ui_plot_window()
            self.uiplotsystem.setupUi(self.windowplotsystem)
            self.toolbar = NavigationToolbar(
                self.uiplotsystem.MplWidget.canvas, self)
            self.toolbar.setStyleSheet("float: flat;\n"
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
            self.windowplotsystem.addToolBar(self.toolbar)
            self.uiplotsystem.MplWidget.canvas.axes.set_xlim(
                [self.x_lim_min, self.x_lim_max])
            self.uiplotsystem.MplWidget.canvas.axes.set_ylim(
                [self.y_lim_min, self.y_lim_max])
            self.uiplotsystem.MplWidget.canvas.axes.grid(self.gridbool)
            self.uiplotsystem.MplWidget.canvas.mpl_connect(
                'button_press_event', self.onclick_plot_initial_system)
            self.uiplotsystem.clearButton.clicked.connect(
                self.display_plot_system)
            self.windowplotsystem.show()

    def onclick_plot_initial_system(self, event):
        if self.toolbar.mode == '':
            #self.__x0 = event.xdata
            #self.__y0 = event.ydata
            self.model.get_initial(event.xdata, event.ydata)
            xnew, ynew, vx_p, vy_p = self.model.rk4()
            self.uiplotsystem.MplWidget.canvas.axes.plot(
                xnew, ynew, color='black')
            self.uiplotsystem.MplWidget.canvas.draw()

    def display_sadle_koef(self):
        if (len(self.mult) == 0):
            self.showDialogerror("необходимо найти мультипликаторы")
        else:
            self.text_koef_sadle.clear()
            self.sadle_number, self.k_sadle1, self.k_sadle2 = self.model.ret_sadle_k()
            for i in range(len(self.sadle_number)):
                self.text_koef_sadle.append(str(self.sadle_number[i] + 1) + ') k1 = ' + str(
                    self.k_sadle1[i]) + ', k2 = ' + str(self.k_sadle2[i]))

    def clear_all(self):
        self.text_fixed.clear()
        self.text_mult.clear()
        self.text_koef_sadle.clear()
        self.model.clear()
        self.x_fixed = []
        self.y_fixed = []
        self.period_fixed = []
        self.k_sadle1 = []
        self.k_sadle2 = []
        self.sadle_number = []

    def find_mult_method(self):
        self.text_mult.clear()
        self.model.find_mult()
        self.mult = self.model.ret_mult()
        if len(self.x_fixed) == 0:
            self.showDialogerror(
                "Необходимо найти неподвижные или периодические точки")
        else:
            for i in range(len(self.x_fixed)):
                self.text_mult.append(
                    str(i + 1) + ') s1 = ' + str(self.mult[i][0]) + ', s2 = ' + str(self.mult[i][1]))

    def display_find_fixed(self):
        if self.indicator_input_system == 0:
            texterror = 'необходимо ввести систему'
            self.showDialogerror(texterror)
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = findfixedwin.Ui_findmultWin()
            self.ui.setupUi(self.window)
            self.ui.findButton.clicked.connect(self.find_fixed_method)
            self.ui.closeButton.clicked.connect(self.window.close)
            self.window.show()

    def find_fixed_method(self):
        self.text_fixed.clear()
        self.model.get_start_fixed(self.ui.xspinBox.value(
        ), self.ui.yspinBox.value())  # начальное предположение
        self.model.find_fixed_point(self.ui.spinBox.value())
        self.period_fixed, self.x_fixed, self.y_fixed = self.model.ret_fixed_points()
        for i in range(len(self.x_fixed)):
            self.text_fixed.append(str(i + 1) + ') (x, y) = (' + str(self.x_fixed[i]) + ', ' + str(self.y_fixed[i]) + ')'
                                   + ',период - ' + str(self.period_fixed[i]) + ';')

    def display_plot_set(self):
        self.windowplotset = QtWidgets.QMainWindow()
        self.uiplotset = setting_plotwin.Ui_settings_plot_window()
        self.uiplotset.setupUi(self.windowplotset)
        self.uiplotset.xmax.setValue(self.x_lim_max)
        self.uiplotset.xmin.setValue(self.x_lim_min)
        self.uiplotset.ymax.setValue(self.y_lim_max)
        self.uiplotset.ymin.setValue(self.y_lim_min)
        self.uiplotset.okButton.clicked.connect(self.setting_plot)
        self.uiplotset.sizepoints.setValue(self.point_size_var)
        self.uiplotset.linetopoint.setChecked(self.linetopoint)
        self.uiplotset.hidepoint.setChecked(self.hidepoints)
        self.uiplotset.checkBox.setChecked(self.gridbool)
        self.uiplotset.checkBox.setStatusTip(
            'применится после перезапуска окна графика')
        self.windowplotset.show()

    def setting_plot(self):
        self.x_lim_min = self.uiplotset.xmin.value()
        self.x_lim_max = self.uiplotset.xmax.value()
        self.y_lim_min = self.uiplotset.ymin.value()
        self.y_lim_max = self.uiplotset.ymax.value()
        self.model.get_limit_plot(self.x_lim_min, self.x_lim_max,
                                  self.y_lim_min, self.y_lim_max)
        if self.uiplotset.checkBox.isChecked():
            self.gridbool = True
        else:
            self.gridbool = False
        if self.uiplotset.comboBox.currentText() == 'черный':
            self.color_points = 'black'
        elif self.uiplotset.comboBox.currentText() == 'красный':
            self.color_points = 'red'
        elif self.uiplotset.comboBox.currentText() == 'зеленый':
            self.color_points = 'green'
        elif self.uiplotset.comboBox.currentText() == 'синий':
            self.color_points = 'blue'

        if self.uiplotset.colorlineCombobox.currentText() == 'черный':
            self.linecolormap = 'black'
        elif self.uiplotset.colorlineCombobox.currentText() == 'красный':
            self.linecolormap = 'red'
        elif self.uiplotset.colorlineCombobox.currentText() == 'зеленый':
            self.linecolormap = 'green'
        elif self.uiplotset.colorlineCombobox.currentText() == 'синий':
            self.linecolormap = 'blue'

        self.point_size_var = self.uiplotset.sizepoints.value()
        self.linetopoint = self.uiplotset.linetopoint.isChecked()
        self.hidepoints = self.uiplotset.hidepoint.isChecked()

    def open_input_system(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = input_systemwin.Ui_inpusystemWin()
        self.ui.setupUi(self.window)
        self.ui.xline.setText(self.textx)
        self.ui.yline.setText(self.texty)
        
        self.window.show()
        self.ui.doubleSpinBox.setValue(self.wp)
        self.ui.oksystem.clicked.connect(self.input_system_user)

    def input_system_user(self):
        if self.ui.xline.text() == '' or self.ui.xline.text() == ' ':
            texterror = 'не введено x`'
            self.showDialogerror(texterror)
        elif self.ui.yline.text == '' or self.ui.yline.text() == ' ':
            texterror = 'не введено y`'
            self.showDialogerror(texterror)
        elif self.ui.doubleSpinBox.value() == 0.0:
            texterror = 'не введена частота возмущения`'
            self.showDialogerror(texterror)
        else:
            self.textx = self.ui.xline.text()
            self.texty = self.ui.yline.text()
            self.wp = self.ui.doubleSpinBox.value()
            self.model.get_input_system(self.textx, self.texty, self.wp)
            self.indicator_input_system = 1
            self.system_and_integrate_display()
            self.window.close()

    def open_setting_integrate(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = integwin.Ui_integrWin()
        self.ui.setupUi(self.window)
        self.ui.spinBox.setValue(self.n)
        self.ui.doubleSpinBox.setValue(self.h)
        self.window.show()
        self.ui.okstep.clicked.connect(self.input_settings_integrate_h)
        self.ui.okiter.clicked.connect(self.input_settings_integrate_iter)

    def input_settings_integrate_h(self):
        self.h = self.ui.doubleSpinBox.value()
        self.model.calculate_data(self.h, self.n)
        self.system_and_integrate_display()

    def input_settings_integrate_iter(self):
        self.n = self.ui.spinBox.value()
        self.model.calculate_data(self.h, self.n)
        self.system_and_integrate_display()

    def open_info_program(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = info.Ui_helpWindow()
        self.ui.setupUi(self.window)
        self.ui.textBrowser.append(self.textinfo)
        self.window.show()

    def newtext(self):
        self.textinfo = '21312'
        self.ui.textBrowser.clear()
        self.ui.textBrowser.append(self.textinfo)

    def system_and_integrate_display(self):
        self.display_system.clear()
        self.display_system.append(
            'x` = ' + self.textx + '\ny` = ' + self.texty)
        self.h, self.n = self.model.ret_integr_set()
        self.display_system.isRightToLeft()
        self.display_system.append('\n__________________________\nпараметры интегрирования:\nшаг: '
                                   + str(self.h) + '\nколичество итераций: '
                                   + str(self.n) + '\nчастота возмущения: ' + str(self.wp))

    def multiP(self):
        if self.indicator_input_system == 0:
            texterror = 'необходимо ввести систему'
            self.showDialogerror(texterror)
        else:
            #threading.Thread(target=self.model.model_plot_initial, args=()).start()
            self.model.model_plot_initial()

    '''
    def multiP(self):
        if self.indicator_input_system == 0:
            texterror = 'необходимо ввести систему'
            self.showDialogerror(texterror)
        else:
            p = Process(None, self.model.model_plot_initial())
            p.start()
     '''

    def showDialogerror(self, texterror):
        QMessageBox.critical(self, "ошибка", texterror)

    def input_model(self, model):
        self.model = model


def main():
    model = Map_wd.Model()
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.input_model(model)
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()


from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
import threading
# используется для нахождения неподвижных или периодических точек
from scipy import optimize
# .................................................математические функции
from math import *
# ..............................................................для array
import numpy as np
# .......................................построение графиков
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


# функция преобразующая строковое выражение в функцию

def symantic_eq(str, x_eq, y_eq, w_perturb, time):
    return eval(str, {'w_p': w_perturb, 'x': x_eq, 'y': y_eq, 't': time,
                      'cos': cos, 'sin': sin, 'tan': tan, 'atan': atan,
                      'exp': exp})


# функция для производной
def diff(var, f, fixed, diff_point, h=1e-10):
    if var == 'xf':
        return (f([diff_point + h / 2, fixed])[0] - f([diff_point - h / 2, fixed])[0]) / h
    elif var == 'xg':
        return (f([diff_point + h / 2, fixed])[1] - f([diff_point - h / 2, fixed])[1]) / h
    elif var == 'yf':
        return (f([fixed, diff_point + h / 2])[0] - f([fixed, diff_point - h / 2])[0]) / h
    elif var == 'yg':
        return (f([fixed, diff_point + h / 2])[1] - f([fixed, diff_point - h / 2])[1]) / h


class Model:

    # ..........конструктор не определен по умолчанию, хотя можно добавить по
    # ..........необходимости
    __x_str = ''  # хранение в строковом формате правой части x: x` = __x_str
    __y_str = ''  # ......................................... y: y` = __y_str
    __w_perturb = .0  # ...........................частота внешнего возмущения
    __h = .01  # ....................шаг интегрирования в методе рунге кутты
    __n = 10000  # .................количество итераций в методе рунге кутты
    __count = ''
    __y0 = .2  # .....начальные условия задаваемые для построения отображения
    __x0 = .4
    __start_fixed = np.zeros(2)
    __x_fixed_p = []  # ................хранение x значений неподвижной точки
    __y_fixed_p = []  # .........................y значений неподвижной точки
    __period_fixed_points = 1  # .......период периодической точки (1 - н.т.)
    __period_fix = []  # .................................хранит периоды точек
    __ar_fixed_points_x = [0] * 2
    __ar_fixed_points_y = [0] * 2
    __save_mult = []
    __k_sadle1 = []  # коэффициенты для касательны седла
    __k_sadle2 = []
    __sadle_number = []  # номер седловой неподвижной точки
    __vx = 0
    __vy = 0
    __vx_p = 0
    __vy_p = 0
    __fig, __ax = None, None  # для взаимодействия с мышь
    __x_lim_min = -10
    __y_lim_min = -10
    __x_lim_max = 10
    __y_lim_max = 10

    def fx(self, x, y, t):
        return symantic_eq(self.__x_str, x, y, self.__w_perturb, t)

    def fy(self, x, y, t):
        return symantic_eq(self.__y_str, x, y, self.__w_perturb, t)

    def get_input_system(self, str_x, str_y, w_perturb):
        self.__x_str = str_x
        self.__y_str = str_y
        self.__w_perturb = w_perturb

    def calculate_data(self, h_inp, n_inp):
        self.__h = h_inp
        self.__n = n_inp

    def get_initial(self, x0, y0):
        self.__x0 = x0
        self.__y0 = y0

    def rk4(self):
        h = self.__h
        n = self.__n
        w_perturb = self.__w_perturb
        #  переобозначеные (x, y) -> (y, z)!!!
        y0 = self.__x0
        z0 = self.__y0

        vy = np.zeros(n)
        vz = np.zeros(n)
        vy[0] = y0
        vz[0] = z0
        t = 0
        step_for_perturb = 0
        vy_p = []
        vz_p = []
        vy_p.append(y0)
        vz_p.append(z0)
        T = 2 * np.pi / w_perturb
        # задает условие на количество итераций, чтобы снимать значение через T
        k = int(T / h)
        for i in range(n - 1):
            k0 = h * self.fx(vy[i], vz[i], t)
            l0 = h * self.fy(vy[i], vz[i], t)
            k1 = h * self.fx(vy[i] + k0 / 2, vz[i] + l0 / 2, t + h / 2)
            l1 = h * self.fy(vy[i] + k0 / 2, vz[i] + l0 / 2, t + h / 2)
            k2 = h * self.fx(vy[i] + k1 / 2, vz[i] + l1 / 2, t + h / 2)
            l2 = h * self.fy(vy[i] + k1 / 2, vz[i] + l1 / 2, t + h / 2)
            k3 = h * self.fx(vy[i] + k2, vz[i] + l2, t)
            l3 = h * self.fy(vy[i] + k2, vz[i] + l2, t)
            vy[i + 1] = vy[i] + (k0 + 2 * k1 + 2 * k2 + k3) / 6
            vz[i + 1] = vz[i] + (l0 + 2 * l1 + 2 * l2 + l3) / 6
            t += h
            if step_for_perturb == k:
                vy_p.append(vy[i + 1])
                vz_p.append(vz[i + 1])
                step_for_perturb = 0
            step_for_perturb += 1
        # определяем границы системы
        # self.__ar_fixed_points_x[0] = vy.min()
        # self.__ar_fixed_points_x[1] = vy.max()
        # self.__ar_fixed_points_y[0] = vz.min()
        # self.__ar_fixed_points_y[1] = vz.max()

        return vy, vz, vy_p, vz_p

    def input_fixed_points_fider(self, x1, x2, y1, y2):
        self.__ar_fixed_points_x[0] = x1
        self.__ar_fixed_points_x[1] = x2
        self.__ar_fixed_points_y[0] = y1
        self.__ar_fixed_points_y[1] = y2

    def calculate_system(self):
        self.__vx, self.__vy, self.__vx_p, self.__vy_p = self.rk4()

    def fixed_point(self, x):
        # ...........Хотя эта функция очень и похожа на rk4, но вводится отдельно для удобства,
        # .................................................нет смысла использовать наследование
        h = self.__h
        w_perturb = self.__w_perturb
        vy = x[0]
        vz = x[1]
        t = 0
        T = 2 * np.pi / w_perturb
        # .задает условие на количество итераций, чтобы снимать значение через T
        k = int(T / h)
        if self.__period_fixed_points == 0:
            k0 = h * self.fx(vy, vz, t)
            l0 = h * self.fy(vy, vz, t)
            k1 = h * self.fx(vy + k0 / 2, vz + l0 / 2, t + h / 2)
            l1 = h * self.fy(vy + k0 / 2, vz + l0 / 2, t + h / 2)
            k2 = h * self.fx(vy + k1 / 2, vz + l1 / 2, t + h / 2)
            l2 = h * self.fy(vy + k1 / 2, vz + l1 / 2, t + h / 2)
            k3 = h * self.fx(vy + k2, vz + l2, t)
            l3 = h * self.fy(vy + k2, vz + l2, t)
            vy += (k0 + 2 * k1 + 2 * k2 + k3) / 6
            vz + (l0 + 2 * l1 + 2 * l2 + l3) / 6
            t += h
        else:
            for i in range(self.__period_fixed_points * k):
                k0 = h * self.fx(vy, vz, t)
                l0 = h * self.fy(vy, vz, t)
                k1 = h * self.fx(vy + k0 / 2, vz + l0 / 2, t + h / 2)
                l1 = h * self.fy(vy + k0 / 2, vz + l0 / 2, t + h / 2)
                k2 = h * self.fx(vy + k1 / 2, vz + l1 / 2, t + h / 2)
                l2 = h * self.fy(vy + k1 / 2, vz + l1 / 2, t + h / 2)
                k3 = h * self.fx(vy + k2, vz + l2, t)
                l3 = h * self.fy(vy + k2, vz + l2, t)
                vy += (k0 + 2 * k1 + 2 * k2 + k3) / 6
                vz + (l0 + 2 * l1 + 2 * l2 + l3) / 6
                t += h
        return [(k0 + 2 * k1 + 2 * k2 + k3) / 6, (l0 + 2 * l1 + 2 * l2 + l3) / 6]

    def for_diff_fixed_point(self, x):
        # ...........Хотя эта функция очень и похожа на rk4, но вводится отдельно для удобства,
        # .................................................нет смысла использовать наследование
        h = self.__h
        w_perturb = self.__w_perturb
        vy = x[0]
        vz = x[1]
        t = 0
        T = 2 * np.pi / w_perturb
        # задает условие на количество итераций, чтобы снимать значение через T
        k = int(T / h)
        if self.__period_fixed_points == 0:
            k0 = h * self.fx(vy, vz, t)
            l0 = h * self.fy(vy, vz, t)
            k1 = h * self.fx(vy + k0 / 2, vz + l0 / 2, t + h / 2)
            l1 = h * self.fy(vy + k0 / 2, vz + l0 / 2, t + h / 2)
            k2 = h * self.fx(vy + k1 / 2, vz + l1 / 2, t + h / 2)
            l2 = h * self.fy(vy + k1 / 2, vz + l1 / 2, t + h / 2)
            k3 = h * self.fx(vy + k2, vz + l2, t)
            l3 = h * self.fy(vy + k2, vz + l2, t)
            vy += (k0 + 2 * k1 + 2 * k2 + k3) / 6
            vz += (l0 + 2 * l1 + 2 * l2 + l3) / 6
            t += h
        else:
            for i in range(self.__period_fixed_points * k):
                k0 = h * self.fx(vy, vz, t)
                l0 = h * self.fy(vy, vz, t)
                k1 = h * self.fx(vy + k0 / 2, vz + l0 / 2, t + h / 2)
                l1 = h * self.fy(vy + k0 / 2, vz + l0 / 2, t + h / 2)
                k2 = h * self.fx(vy + k1 / 2, vz + l1 / 2, t + h / 2)
                l2 = h * self.fy(vy + k1 / 2, vz + l1 / 2, t + h / 2)
                k3 = h * self.fx(vy + k2, vz + l2, t)
                l3 = h * self.fy(vy + k2, vz + l2, t)
                vy += (k0 + 2 * k1 + 2 * k2 + k3) / 6
                vz += (l0 + 2 * l1 + 2 * l2 + l3) / 6
                t += h
        return [vy, vz]

    # метод find_fixed_points используется для поиска неподвижной точки или периодической точки
    # он перегружен на поиск неподвижной точки или неподвижных точек в диапазоне
    def get_start_fixed(self, x_0, y_0):
        self.__start_fixed[0] = x_0
        self.__start_fixed[1] = y_0

    def get_period_fixed_points(self, period):  # для задания периода
        self.__period_fixed_points = period

    #  нахождение неподвижной или период. точки (уточнение пользователя)
    def find_fixed_point(self, period):
        self.__period_fixed_points = period
        fixed = optimize.fsolve(self.fixed_point, self.__start_fixed)
        test = 0
        if len(self.__x_fixed_p) > 0:
            for i in range(len(self.__x_fixed_p)):
                if abs(self.__x_fixed_p[i] - fixed[0]) < 1e-4 and abs(self.__y_fixed_p[i] - fixed[1]) < 1e-4:
                    test = 1
                    break
        if test == 0:
            self.__x_fixed_p.append(fixed[0])
            self.__y_fixed_p.append(fixed[1])
            self.__period_fix.append(period)

    # нахождение всех периодических точек периода period
    def find_fixed_points_p(self, period, step=.001):
        # h - шаг поиска
        self.__period_fixed_points = period
        step_x = int(
            abs(self.__ar_fixed_points_x[1] - self.__ar_fixed_points_x[0]) / step)
        step_y = int(
            abs(self.__ar_fixed_points_y[1] - self.__ar_fixed_points_y[0]) / step)
        for i in range(step_x):
            for j in range(step_y):
                x_f = self.__ar_fixed_points_x[0] + i * step
                y_f = self.__ar_fixed_points_y[0] + j * step
                self.get_start_fixed(x_f, y_f)
                fixed = optimize.fsolve(self.fixed_point, self.__start_fixed)
                test = 0
                if len(self.__x_fixed_p) != 0:
                    for k in range(len(self.__x_fixed_p)):
                        if (- 1e-10 < abs(self.__x_fixed_p[k] - fixed[0]) < 1e8
                                and - 1e-10 < abs(self.__y_fixed_p[k] - fixed[1]) < 1e-8):
                            test = 1
                            break
                if test == 0:
                    self.__x_fixed_p.append(fixed[0])
                    self.__y_fixed_p.append(fixed[1])
                    self.__period_fix.append(period)

    # метод find_mult используется для поиска мультипликаторов неподвижной
    # или периодической точки
    def find_mult(self):
        self.__save_mult = []
        self.__k_sadle1 = []
        self.__k_sadle2 = []
        self.__sadle_number = []
        step = len(self.__x_fixed_p)
        for i in range(step):
            x_0 = self.__x_fixed_p[i]
            y_0 = self.__y_fixed_p[i]
            dfx = diff('xf', self.for_diff_fixed_point, y_0, x_0)
            dgx = diff('xg', self.for_diff_fixed_point, y_0, x_0)
            dfy = diff('yf', self.for_diff_fixed_point, x_0, y_0)
            dgy = diff('yg', self.for_diff_fixed_point, x_0, y_0)
            # mu = symbols('mu')
            # solve(mu ** 2 - mu * (dfx + dgy) + (dfx * dgy - dfy * dgx), mu)
            eq = np.linalg.eig([[dfx, dfy], [dgx, dgy]])

            mult = np.linalg.eig([[dfx, dfy], [dgx, dgy]])[0]
            self.__save_mult.append(mult)

            if type(mult[0]) != np.complex128:
                if( (abs(mult[0]) > 1 and abs(mult[1]) < 1) or (abs(mult[0]) < 1 and abs(mult[1]) > 1)):
                    self.__sadle_number.append(i)
                    self.__k_sadle1.append(eq[1][0][1] / eq[1][0][0])
                    self.__k_sadle2.append(eq[1][1][0] / eq[1][1][1])

    def display_mult(self):
        step = len(self.__x_fixed_p)
        for i in range(step):
            x = self.__x_fixed_p[i]
            y = self.__y_fixed_p[i]
            print('н.т.: (', round(x, 10), ', ', round(y, 10), ')',
                  'мультипликаторы: ', self.__save_mult[i])

    def display_fixed_points(self):
        step = len(self.__y_fixed_p)
        for i in range(step):
            x = self.__x_fixed_p[i]
            y = self.__y_fixed_p[i]
            print('(x_', i, ', y_', i, ') = ', round(x, 10), ', ',
                  round(y, 10), ', ее период: ', self.__period_fix[i])

    #  отображение коэффициентов у седла
    def display_sadle_k(self):
        step = len(self.__sadle_number)
        if step != 0:
            j = 0
            for i in self.__sadle_number:
                print('н.т:(', self.__x_fixed_p[i], ', ', self.__y_fixed_p[i], ')',
                      'коэффициенты наклона: k1 = ', self.__k_sadle1[j], ', k2 = ', self.__k_sadle2)
                j += 1

    def ret_sadle_k(self):
        return self.__sadle_number, self.__k_sadle1, self.__k_sadle2

    # следующий метод 'model_plot' позволяет строить графики:
    # два в одном окне
    # только систему и только отображение
    # систему и отображение на одном графике
    def model_plot(self, count_plot='system_and_map'):
        xnew, ynew, vx_p, vy_p = self.rk4()
        plt.figure(figsize=(10, 5))
        if count_plot == 'system_and_map':
            plt.subplot(121)
            plt.plot(xnew, ynew)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title("system")
            plt.subplot(122)
            plt.plot(vx_p, vy_p, '.')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title("map")
        elif count_plot == 'system':
            plt.plot(xnew, ynew)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title("system")
        elif count_plot == 'map':
            plt.plot(vx_p, vy_p, '.')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title("map")
        elif count_plot == 'map_and_system_one_plot':
            plt.plot(xnew, ynew)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.plot(vx_p, vy_p, '.')
            plt.xlabel('x')
            plt.ylabel('y')
        plt.show()

    def get_limit_plot(self, xmin, xmax, ymin, ymax):
        self.__x_lim_min = xmin
        self.__x_lim_max = xmax
        self.__y_lim_min = ymin
        self.__y_lim_max = ymax

    def model_plot_initial(self):
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(111)
        #self.__fig, self.__ax = plt.subplots()
        cid = self.__fig.canvas.mpl_connect(
            'button_press_event', self.onclick_plot_initial)
        plt.grid(True)
        plt.xlim([self.__x_lim_min, self.__x_lim_max])
        plt.ylim([self.__y_lim_min, self.__y_lim_max])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('map')
        plt.show()

    def onclick_plot_initial(self, event):

        toolbar = plt.get_current_fig_manager().toolbar
        if toolbar.mode == '':  # проверка, если нажата кнопка, то событие не считывается
            self.__x0 = event.xdata
            self.__y0 = event.ydata
            xnew, ynew, vx_p, vy_p = self.rk4()
            for i in range(len(vx_p)):
                #plt.plot(vx_p[i], vy_p[i], '.', color='black')
                plt.scatter(vx_p[i], vy_p[i], s=1, color='black')
                self.__fig.canvas.draw()

    def new_w_p(self, w_p):
        self.__w_perturb = w_p

    def clear(self):
        self.__count = ''
        self.__y0 = .2  # .....начальные условия задаваемые для построения отображения
        self.__x0 = .4
        self.__start_fixed = np.zeros(2)
        self.__x_fixed_p = []  # ................хранение x значений неподвижной точки
        self.__y_fixed_p = []  # .........................y значений неподвижной точки
        # .......период периодической точки (1 - н.т.)
        self.__period_fixed_points = 1
        self.__period_fix = []  # .................................хранит периоды точек
        self.__ar_fixed_points_x = [0] * 2
        self.__ar_fixed_points_y = [0] * 2
        self.__save_mult = []
        self.__k_sadle1 = []  # коэффициенты для касательны седла
        self.__k_sadle2 = []
        self.__sadle_number = []  # номер седловой неподвижной точки
        self.__vx = 0
        self.__vy = 0
        self.__vx_p = 0
        self.__vy_p = 0

    def display_str(self):
        print(self.__y_str)
        print(self.__x_str)

    def ret_integr_set(self):
        n = self.__n
        h = self.__h
        return h, n

    def ret_fixed_points(self):
        return self.__period_fix, self.__x_fixed_p, self.__y_fixed_p

    def ret_mult(self):
        return self.__save_mult

from PyQt5 import QtWidgets
from frontend import main_window, Two_Dim_System
from PyQt5.QtWidgets import QInputDialog, qApp
from frontend import input_system
from PyQt5.QtWidgets import *
import sys, os
from qt_material import apply_stylesheet
from frontend import start_window
from qt_material import apply_stylesheet

# from frontend import two_D_plot_window
style_sheets = ['dark_amber.xml',
                'dark_blue.xml',
                'dark_cyan.xml',
                'dark_lightgreen.xml',
                'dark_pink.xml',
                'dark_purple.xml',
                'dark_red.xml',
                'dark_teal.xml',
                'dark_yellow.xml',
                'light_amber.xml',
                'light_blue.xml',
                'light_cyan.xml',
                'light_cyan_500.xml',
                'light_lightgreen.xml',
                'light_pink.xml',
                'light_purple.xml',
                'light_red.xml',
                'light_teal.xml',
                'light_yellow.xml']
os.environ['QT_API'] = 'pyqt5'
os.environ["QT_FONT_DPI"] = "96"


class App(QtWidgets.QMainWindow, input_system.Ui_input_system, start_window.Ui_NS_startup):
    def __init__(self):
        super().__init__()
        self.ui = start_window.Ui_NS_startup()
        self.ui.setupUi(self)
        self.InitUi()

    def InitUi(self):
        self.ui.twoDsystem.clicked.connect(self.two_D_system_start)

    def two_D_system_start(self):
        # self.window = QtWidgets.QMainWindow()
        self.ui = Two_Dim_System.Two_Dim_system()
        self.ui.show()


def main():
    app = QtWidgets.QApplication(sys.argv)  # new  QApplication
    theme_number = 0
    if not os.path.exists('config_theme'):
        with open('config_theme', 'w') as file:
            file.write('0')
    with open('config_theme') as file:
        theme_number = int(file.readline()[0])
        if theme_number > len(style_sheets):
            theme_number = 0

    apply_stylesheet(app, theme=style_sheets[theme_number])

    window = App()  # Create object ExampleApp
    window.show()  # ???????????????????? ????????
    app.exec_()  # ?? ?????????????????? ????????????????????


if __name__ == '__main__':  # ???????? ???? ?????????????????? ???????? ????????????????, ?? ???? ??????????????????????
    main()  # ???? ?????????????????? ?????????????? main()

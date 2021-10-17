"""AI is creating summary for 
"""

from frontend import main_window
from PyQt5 import QtWidgets
from frontend import input_system
from PyQt5.QtWidgets import QInputDialog, qApp
from qt_material import apply_stylesheet

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


class Two_Dim_system(QtWidgets.QMainWindow, main_window.Ui_MainWindow, input_system.Ui_input_system):
    """AI is creating summary for App

    Args:
        QtWidgets ([type]): [description]
        main_window ([type]): [description]
    """

    def __init__(self):
        """AI is creating summary for __init__
        """
        super().__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.InitUI()

    def InitUI(self):
        """AI is creating summary for setupUi
        """
        self.setupUi(self)
        # self.statusBar = QStatusBar()
        # self.setStatusBar(self.statusBar)
        # self.menuFile.setStatusTip()
        # self.menuFile.setStatusTip("test")
        self.actionExit.triggered.connect(qApp.quit)
        self.darkamber.triggered.connect(lambda: self.__change_theme(style_sheets.index('dark_amber.xml')))
        self.lightamber.triggered.connect(lambda: self.__change_theme(style_sheets.index('light_amber.xml')))
        self.darkblue.triggered.connect(lambda: self.__change_theme(style_sheets.index('dark_blue.xml')))
        self.lightblue.triggered.connect(lambda: self.__change_theme(style_sheets.index('light_blue.xml')))
        self.darkcyan.triggered.connect(lambda: self.__change_theme(style_sheets.index('dark_cyan.xml')))
        self.lightcyan.triggered.connect(lambda: self.__change_theme(style_sheets.index('light_cyan.xml')))
        self.darklightgreen.triggered.connect(lambda: self.__change_theme(style_sheets.index('dark_lightgreen.xml')))
        self.lightlightgreen.triggered.connect(lambda: self.__change_theme(style_sheets.index('light_lightgreen.xml')))
        self.darkpink.triggered.connect(lambda: self.__change_theme(style_sheets.index('dark_pink.xml')))
        self.lightping.triggered.connect(lambda: self.__change_theme(style_sheets.index('light_pink.xml')))
        self.darkpurple.triggered.connect(lambda: self.__change_theme(style_sheets.index('dark_purple.xml')))
        self.lightpurple.triggered.connect(lambda: self.__change_theme(style_sheets.index('light_purple.xml')))
        self.darkred.triggered.connect(lambda: self.__change_theme(style_sheets.index('dark_red.xml')))
        self.lightred.triggered.connect(lambda: self.__change_theme(style_sheets.index('light_red.xml')))
        self.darkteal.triggered.connect(lambda: self.__change_theme(style_sheets.index('dark_teal.xml')))
        self.lightteal.triggered.connect(lambda: self.__change_theme(style_sheets.index('light_teal.xml')))
        self.darkyellow.triggered.connect(lambda: self.__change_theme(style_sheets.index('dark_yellow.xml')))
        self.lightyellow.triggered.connect(lambda: self.__change_theme(style_sheets.index('light_yellow.xml')))
        self.actionInput_system.triggered.connect(self.__input_system)

    def __input_system(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = input_system.Ui_input_system()
        self.ui.setupUi(self.window)
        self.window.show()

    def __change_theme(self, number: int):
        """AI is creating summary for change_theme

        Args:
            number (int): [description]
        """
        with open('config_theme', 'w') as file:
            file.write(str(number))
        apply_stylesheet(self, theme=style_sheets[number])
        print('TEST')

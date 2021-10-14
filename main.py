"""AI is creating summary for 
"""

from PyQt5 import QtWidgets
from frontend import main_window
from PyQt5.QtWidgets import QInputDialog, qApp
from PyQt5.QtWidgets import*
import sys, os
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
os.environ['QT_API'] = 'pyqt5'
os.environ["QT_FONT_DPI"] = "96"



class App(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
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
        #self.statusBar = QStatusBar()
        #self.setStatusBar(self.statusBar)
        #self.menuFile.setStatusTip()
        self.menuFile.setStatusTip("test")
        self.actionExit.triggered.connect(qApp.quit)
        self.darkamber.triggered.connect(lambda: self.__change_theme(style_sheets.index('dark_amber.xml')))
        self.lightamber.triggered.connect(lambda: self.__change_theme(style_sheets.index('light_amber.xml')))
        self.darkblue.triggered.connect(lambda: self.__change_theme(style_sheets.index('dark_blue.xml')))
        self.lightblue.triggered.connect(lambda: self.__change_theme(style_sheets.index('light_blue.xml')))
        self.darkcyan.triggered.connect(lambda: self.__change_theme(style_sheets.index('dark_cyan.xml')))
        self.lightcyan.triggered.connect(lambda: self.__change_theme(style_sheets.index('light_cyan.xml')))

    def __change_theme(self, number:int):
        """AI is creating summary for change_theme

        Args:
            number (int): [description]
        """
        with open('config_theme', 'w') as file:
            file.write(str(number))
        apply_stylesheet(self, theme=style_sheets[number])

    
        
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
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()   
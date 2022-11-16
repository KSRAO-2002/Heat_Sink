import sys
import os
from PySide2 import *
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from qt_material import *

#IMPORT GUI FILE
from final import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        apply_stylesheet(app, theme='dark_blue.xml')

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(Qt.green)

 
        self.ui.centralwidget.setGraphicsEffect(self.shadow)


        self.setWindowIcon(QtGui.QIcon(":/Black/Icons/white/airplay.svg"))

        self.setWindowTitle("HEATSINK")
        QSizeGrip(self.ui.size_grip)      
        #minimize window
        self.ui.Minimize_window_button.clicked.connect(lambda:self.showMinimized())

        #close window
        self.ui.Close_window_button.clicked.connect(lambda:self.close())

        #restore/maximize window
        self.ui.Restore_window_button.clicked.connect(lambda: self.resize_win())

        
        self.show()

    #minimized
    def resize_win(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.Restore_window_button.setIcon(QtGui.QIcon(u":/Black/Icons/white/plus-square.svg"))
        else:
            self.showMaximized()
            self.ui.Restore_window_button.setIcon(QtGui.QIcon(u":/Black/Icons/white/minus-square.svg"))

## Execute App

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

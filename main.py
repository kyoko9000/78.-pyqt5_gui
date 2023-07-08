# ************************** man hinh loai 2 *************************
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        height = self.uic.centralwidget.parent().height()
        width = self.uic.centralwidget.parent().width()
        print("main size", height, width)
        self.uic.label.setGeometry(QtCore.QRect(0, 0, width, height))

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            state = int(self.windowState())
            if state == 0:
                print("WindowMinimized")
                height = self.uic.centralwidget.parent().height()
                width = self.uic.centralwidget.parent().width()
                self.uic.label.setPixmap(QtGui.QPixmap("1.jpg"))
                self.uic.label.setGeometry(QtCore.QRect(0, 0, width, height))

            elif self.isMaximized():
                print("WindowMaximized")
                height = self.uic.centralwidget.parent().height()
                width = self.uic.centralwidget.parent().width()
                self.uic.label.setPixmap(QtGui.QPixmap("2.jpg"))
                self.uic.label.setGeometry(QtCore.QRect(0, 0, width, height))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
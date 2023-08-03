# ************************** man hinh loai 2 *************************
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSize
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from gui2 import Ui_MainWindow
from screen_1 import add_screen_1, add_screen_2


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.me)
        self.uic.pushButton_2.clicked.connect(self.other)

    def me(self):
        text = self.uic.textEdit.toPlainText()
        newitem = QListWidgetItem()
        newitem.setSizeHint(QSize(0, 60))
        centralwidget = add_screen_1(text)
        self.uic.listWidget.addItem(newitem)
        self.uic.listWidget.setItemWidget(newitem, centralwidget)
        self.uic.listWidget.scrollToBottom()

    def other(self):
        text = self.uic.textEdit.toPlainText()
        newitem = QListWidgetItem()
        newitem.setSizeHint(QSize(0, 60))

        centralwidget = add_screen_2(text)

        self.uic.listWidget.addItem(newitem)
        self.uic.listWidget.setItemWidget(newitem, centralwidget)
        self.uic.listWidget.scrollToBottom()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

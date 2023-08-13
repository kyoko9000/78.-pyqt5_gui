import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSize
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from gui2 import Ui_MainWindow


def add_screen_1(text):
    centralwidget = QtWidgets.QWidget()
    centralwidget.setObjectName("centralwidget")
    horizontalLayout = QtWidgets.QHBoxLayout(centralwidget)
    horizontalLayout.setContentsMargins(0, 0, 0, -1)
    horizontalLayout.setSpacing(0)
    horizontalLayout.setObjectName("horizontalLayout")
    label = QtWidgets.QLabel(centralwidget)
    label.setMaximumSize(QtCore.QSize(50, 50))
    label.setStyleSheet("QLabel{\n"
                        "border-image: url(\'1.jpg\');\n"
                        "border-radius: 25px;\n"
                        "}")
    label.setText("")
    label.setObjectName("label")
    horizontalLayout.addWidget(label)
    frame_2 = QtWidgets.QFrame(centralwidget)
    frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_2.setObjectName("frame_2")
    horizontalLayout_3 = QtWidgets.QHBoxLayout(frame_2)
    horizontalLayout_3.setContentsMargins(40, 0, 0, 0)
    horizontalLayout_3.setSpacing(0)
    horizontalLayout_3.setObjectName("horizontalLayout_3")
    label_2 = QtWidgets.QLabel(frame_2)
    label_2.setText(text)
    label_2.setObjectName("label_2")
    horizontalLayout_3.addWidget(label_2)
    horizontalLayout.addWidget(frame_2)
    return centralwidget


def add_screen_2(text):
    centralwidget = QtWidgets.QWidget()
    centralwidget.setObjectName("centralwidget")
    horizontalLayout = QtWidgets.QHBoxLayout(centralwidget)
    horizontalLayout.setContentsMargins(0, 0, 0, 0)
    horizontalLayout.setSpacing(0)
    horizontalLayout.setObjectName("horizontalLayout")
    frame = QtWidgets.QFrame(centralwidget)
    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame.setFrameShadow(QtWidgets.QFrame.Raised)
    frame.setObjectName("frame")
    horizontalLayout_2 = QtWidgets.QHBoxLayout(frame)
    horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
    horizontalLayout_2.setSpacing(0)
    horizontalLayout_2.setObjectName("horizontalLayout_2")
    frame_2 = QtWidgets.QFrame(frame)
    frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_2.setObjectName("frame_2")
    horizontalLayout_3 = QtWidgets.QHBoxLayout(frame_2)
    horizontalLayout_3.setContentsMargins(0, 0, 40, 0)
    horizontalLayout_3.setSpacing(0)
    horizontalLayout_3.setObjectName("horizontalLayout_3")
    label_2 = QtWidgets.QLabel(frame_2)
    label_2.setText(text)
    label_2.setObjectName("label_2")
    horizontalLayout_3.addWidget(label_2)
    horizontalLayout_2.addWidget(frame_2)
    label = QtWidgets.QLabel(frame)
    label.setMaximumSize(QtCore.QSize(50, 50))
    label.setStyleSheet("QLabel{\n"
                        "border-image: url(\'2.jpg\');\n"
                        "border-radius: 25px;\n"
                        "}")
    label.setText("")
    label.setObjectName("label")
    horizontalLayout_2.addWidget(label)
    horizontalLayout.addWidget(frame)
    return centralwidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.me)
        self.uic.pushButton_2.clicked.connect(self.other)

    def me(self):
        text = self.uic.textEdit.toPlainText()
        baseitem = QListWidgetItem()
        baseitem.setSizeHint(QSize(0, 60))

        item = add_screen_1(text)
        self.uic.listWidget.addItem(baseitem)
        self.uic.listWidget.setItemWidget(baseitem, item)
        self.uic.listWidget.scrollToBottom()

    def other(self):
        text = self.uic.textEdit.toPlainText()
        baseitem = QListWidgetItem()
        baseitem.setSizeHint(QSize(0, 60))

        item = add_screen_2(text)
        self.uic.listWidget.addItem(baseitem)
        self.uic.listWidget.setItemWidget(baseitem, item)
        self.uic.listWidget.scrollToBottom().


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

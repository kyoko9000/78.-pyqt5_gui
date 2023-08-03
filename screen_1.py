from PyQt5 import QtWidgets, QtCore


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
    label.setText("hello \n toi van khoe")
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
    centralwidget.setObjectName("centralwidget1")
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
    horizontalLayout_3.setContentsMargins(40, 0, 0, 0)
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

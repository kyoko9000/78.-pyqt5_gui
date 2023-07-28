import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem
from gui1 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        # department_1 = QTreeWidgetItem(self.uic.treeWidget)
        # department_1.setText(0, 'Sales')
        # department_2 = QTreeWidgetItem(self.uic.treeWidget)
        # department_2.setText(0, 'Marketing')
        # department_3 = QTreeWidgetItem(self.uic.treeWidget)
        # department_3.setText(0, 'HR')
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("3.jpg"))
        # department_3.setIcon(0, icon)
        #
        # leader_1 = QTreeWidgetItem()
        # leader_1.setText(0, 'John')
        # department_1.addChild(leader_1)
        # leader_2 = QTreeWidgetItem()
        # leader_2.setText(0, 'Jane')
        # department_1.addChild(leader_2)
        #
        # worker_1 = QTreeWidgetItem()
        # worker_1.setText(0, 'tom')
        # leader_1.addChild(worker_1)
        # worker_2 = QTreeWidgetItem()
        # worker_2.setText(0, 'jerry')
        # leader_1.addChild(worker_2)

        departments = ['Sales', 'Marketing', 'HR']
        employees = {
            'Sales': ['John', 'Jane', 'Peter'],
            'Marketing': ['Alice', 'Bob'],
            'HR': ['David'],
        }

        for department in departments:
            department_item = QTreeWidgetItem(self.uic.treeWidget)
            department_item.setText(0, department)

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("3.jpg"))
            department_item.setIcon(0, icon)
            # set the children
            for employee in employees[department]:
                employee_item = QTreeWidgetItem()
                employee_item.setText(0, employee)
                department_item.addChild(employee_item)

                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("4.jpg"))
                employee_item.setIcon(0, icon1)

        self.uic.treeWidget.itemClicked.connect(self.show_signal)

    def show_signal(self, x, col):
        print(x.text(col), col)
        if x.text(col) == "John":
            print(f"{x.text(col)} do something")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

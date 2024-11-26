import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableView
from SSHmealDesignerPython import Ui_Dialog  
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

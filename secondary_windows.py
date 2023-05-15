import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QButtonGroup, QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import QtWidgets, QtGui

from auth_win import Ui_auth_win
from genjson import Ui_Form2
from path import Ui_PathWin
from ent_win import Ui_login
from reg_win import Ui_login2
from main_windows import AddWin


class Auth(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_auth_win()
        self.ui.setupUi(self)

        self.ui.auth.clicked.connect(self.open_ent)
        self.ui.reg.clicked.connect(self.open_reg)

    def open_ent(self):
        self.w = Ent()
        self.w.show()
        self.close()

    def open_reg(self):
        self.w = Reg()
        self.w.show()
        self.close()


class Ent(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)

        self.ui.pb_home.clicked.connect(self.back_home)
        self.ui.pb_done.clicked.connect(self.done)

    def back_home(self):
        self.w = Auth()
        self.w.show()
        self.close()

    def done(self):
        self.w = MainWin()
        self.w.show()
        self.close()


class Reg(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login2()
        self.ui.setupUi(self)

        self.ui.pb_home.clicked.connect(self.back_home)
        self.ui.pb_done.clicked.connect(self.done)

    def back_home(self):
        self.w = Auth()
        self.w.show()
        self.close()

    def done(self):
        self.w = MainWin()
        self.w.show()
        self.close()


class MainWin(QWidget):
    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = Ui_Form2()
        self.ui.setupUi(self)
        self.ui.add_2.clicked.connect(self.create_win_path)

    def create_win_path(self):
        self.close()
        self.w = PathWin()

        self.w.show()

class ErrorWin:
    def __init__(self, message=None):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка!")
        if message == None:
            msg.setInformativeText('Заполните правильно все поля ввода.')
        else:
            msg.setInformativeText(message)
        msg.setWindowTitle("Внимание!")
        msg.exec_()


class PathWin(QWidget):
    def __init__(self):
        super(PathWin, self).__init__()
        self.ui = Ui_PathWin()
        self.ui.setupUi(self)

        self.ui.pb_browse.clicked.connect(self.getting_path)
        self.ui.pb_done.clicked.connect(self.done)

    def getting_path(self):
        self.path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Укажите папку')
        self.ui.le_path.setText(self.path)

    def done(self):
        self.namejson = self.ui.le_filename.text()
        path = self.ui.le_path.text()
        if self.namejson != '' and os.path.exists(path):
            self.create_win_add()
        else:
            self.ui.le_path.setText('')
            ErrorWin()

    def create_win_add(self):
        self.w = AddWin()

        self.w.show()
        self.close()


app = QApplication(sys.argv)
# application = Auth()
application = AddWin()
application.show()
sys.exit(app.exec())
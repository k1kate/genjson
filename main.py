import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QButtonGroup, QWidget, QMessageBox
from PyQt5 import QtWidgets, QtGui

from genjson import Ui_Form2
from list_of_test import Ui_list_of_test
from test_form import Ui_Form
from path import Ui_PathWin
from necessary_test import Ui_necessary_test


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
    def __init__(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка!")
        msg.setInformativeText('Заполните правильно все поля ввода.')
        msg.setWindowTitle("Внимание!")
        msg.exec_()


class NecessWin(QWidget):
    def __init__(self, llist, parent=None):
        super(NecessWin, self).__init__()
        self.ui = Ui_necessary_test()
        self.ui.setupUi(self)

        self.llist = llist
        self.list_obj = []
        self.list_selected_groups = []
        self.parrent = parent

        self.draw_wid()

        self.ui.done.clicked.connect(self.done)

    def draw_wid(self):
        for group in range(len(self.llist)):
            cb = QtWidgets.QCheckBox('{} группа'.format(self.llist[group]))
            cb.setFont(QtGui.QFont('Consolas', 10))
            cb.stateChanged.connect(lambda state, x=self.llist[group]: self.add_in_list(state, x))
            self.ui.formLayout.addWidget(cb)

    def add_in_list(self, state, gr):
        if gr not in self.list_selected_groups:
            self.list_selected_groups.append(gr)
        else:
            self.list_selected_groups.remove(gr)

    def done(self):
        # for i in self.list_obj:
        #     if i.isChecked():
        #         print(i)

        self.close()


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
        self.close()
        self.w = AddWin(self)

        self.w.show()


class AddWin(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_list_of_test()
        self.ui.setupUi(self)
        self.parrent = parent
        self.counter = 0
        self.row_for_tests_1 = 0
        self.row_for_tests_2 = 0
        self.list_of_groups = []
        self.dict_of_tests = {}
        self.counter_of_elem_grid1 = 0
        self.is_first_test = False
        self.past_limitation = ''
        self.group_num = 1
        self.path = self.parrent.path
        # self.path = r'C:\Users\катя\Desktop\genjson\тест'

        self.ui.label.setFixedSize(850, 67)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(11)

        self.pushb_2_add = QtWidgets.QPushButton('Добавить')
        self.pushb_2_add.setFixedSize(180, 30)
        self.pushb_2_add.setFont(QtGui.QFont('Consolas', 10))

        self.ui.pushb_1_add.clicked.connect(lambda: self.add_test(1))
        self.pushb_2_add.clicked.connect(lambda: self.add_test(2))

    def add_test(self, btn): # окно со списками тестов
        self.w = FormWin(btn, self)

        self.w.show()


class FormWin(QWidget):
    def __init__(self, btn, parent=None):
        super(FormWin, self).__init__()
        self.parrent = parent
        self.btn = btn
        self.list_selected_groups = []

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        if self.parrent.counter == 0 or self.parrent.counter_of_elem_grid1 == 0 or self.parrent.counter == 1:
            self.ui.radioButton_7.setEnabled(False)
            if self.parrent.counter == 0:
                self.ui.lineEdit_19.setEnabled(False)
                self.scores = '0'

        self.group_rb = QButtonGroup()
        self.group_rb.addButton(self.ui.radioButton_7)
        self.group_rb.addButton(self.ui.radioButton_8)
        self.group_rb.buttonClicked.connect(self.limit)

        self.ui.pushButton.clicked.connect(self.done)

        if self.parrent.row_for_tests_1 != 0 and self.parrent.row_for_tests_2 != 0:
             self.ui.pushButton_2.clicked.connect(self.necessarytest)

    def necessarytest(self):
        self.w = NecessWin(self.parrent.list_of_groups, self)

        self.w.show()

    def done(self):
        self.test_filename = self.ui.lineEdit_16.text()
        self.limitation = self.ui.lineEdit_17.text()
        self.data_in = self.ui.plainTextEdit_7.toPlainText()
        self.data_out = self.ui.plainTextEdit_8.toPlainText()

        if self.parrent.is_first_test != 0:
            self.scores = self.ui.lineEdit_19.text()

        if self.test_filename != '' and \
                self.data_in != '' and \
                self.data_out != '' and \
                self.scores != '' and \
                self.scores.isdigit() and \
                (self.ui.radioButton_7.isChecked() or (self.ui.radioButton_8.isChecked() and self.limitation != '')):

            self.parrent.counter += 1

            if self.parrent.counter == 1 and (not self.parrent.is_first_test):
                self.create_second_header()

            self.adding_test_to_list()

            if self.ui.radioButton_8.isChecked() and self.parrent.counter > 1:
                self.group.setText('группа: {}'.format(self.parrent.group_num))
                self.parrent.list_of_groups.append(str(self.parrent.group_num))
                self.parrent.group_num += 1
            elif self.ui.radioButton_7.isChecked():
                self.parrent.dict_of_tests.get(self.parrent.counter)[6] = self.parrent.dict_of_tests[self.parrent.counter - 1][6]

            self.create_test_file()

            self.close()

        else:
            ErrorWin()

    def create_test_file(self):
        f_in = open(r'{}\{}.txt'.format(self.parrent.path, self.test_filename), 'w')
        f_out = open(r'{}\{}a.txt'.format(self.parrent.path, self.test_filename), 'w')
        f_in.write(self.data_in)
        f_out.write(self.data_out)

    def create_second_header(self):
        self.main_head_lb = QLabel('Основные тесты:')
        self.main_head_lb.setFont(QtGui.QFont('Consolas', 25))
        self.main_head_lb.setFixedSize(400, 67)
        self.parrent.ui.verticalLayout_4.addWidget(self.main_head_lb)
        self.parrent.ui.verticalLayout_4.addWidget(self.parrent.pushb_2_add)
        self.parrent.ui.verticalLayout_4.addLayout(self.parrent.gridLayout_3)

        self.parrent.ui.pushb_1_add.hide()

        self.parrent.is_first_test = True

    def delete_test(self, btn):
        for id, list in self.parrent.dict_of_tests.items():
            if list[2] == btn:
                btn.hide()
                list[1].hide()
                list[0].hide()
                list[3].hide()
                self.parrent.counter -= 1
                os.remove(r'{}\{}.txt'.format(self.parrent.path, self.test_filename))
                os.remove(r'{}\{}a.txt'.format(self.parrent.path, self.test_filename))

        if self.btn == 1:
            self.parrent.counter_of_elem_grid1 -= 1
            self.parrent.pushb_2_add.setEnabled(False)

    def drawing_tests_in_list(self):
        self.name_of_test = QLabel(self.test_filename)
        self.group = QLabel()
        self.pb_edit = QtWidgets.QPushButton('Редактировать')
        self.pb_del = QtWidgets.QPushButton('Удалить')

        self.name_of_test.setFont(QtGui.QFont('Consolas', 10))
        self.group.setFont(QtGui.QFont('Consolas', 10))
        self.pb_edit.setFont(QtGui.QFont('Consolas', 10))
        self.pb_del.setFont(QtGui.QFont('Consolas', 10))

        self.pb_edit.setFixedSize(150, 35)
        self.pb_del.setFixedSize(150, 35)

        self.pb_del.clicked.connect(lambda state, btn=self.pb_del: self.delete_test(btn))

        if self.parrent.counter_of_elem_grid1 == 0:
            self.parrent.dict_of_tests[1] = [self.name_of_test, self.pb_edit, self.pb_del, self.group, 0, 0, self.limitation, False]
        elif self.ui.radioButton_8.isChecked():
            self.parrent.dict_of_tests[self.parrent.counter] = [self.name_of_test, self.pb_edit, self.pb_del, self.group, self.parrent.group_num, self.scores, self.limitation, True]
        else:
            self.parrent.dict_of_tests[self.parrent.counter] = [self.name_of_test, self.pb_edit, self.pb_del,
                                                                self.group, self.parrent.group_num-1, self.scores, '', False]


    def adding_test_to_list(self):
        self.drawing_tests_in_list()

        if self.btn == 1:
            self.grid = self.parrent.ui.gridLayout_2
            row = self.parrent.row_for_tests_1
            self.parrent.counter_of_elem_grid1 += 1
            self.parrent.pushb_2_add.setEnabled(True)

        else:
            self.grid = self.parrent.gridLayout_3
            row = self.parrent.row_for_tests_2

        self.grid.addWidget(self.name_of_test, row, 0)
        if self.parrent.counter_of_elem_grid1 != 0:
            self.grid.addWidget(self.group, row, 1)
        self.grid.addWidget(self.pb_edit, row, 2)
        self.grid.addWidget(self.pb_del, row, 3)

        if self.btn == 1:
            self.parrent.row_for_tests_1 += 1
        else:
            self.parrent.row_for_tests_2 += 1

        if self.parrent.counter_of_elem_grid1 == 1:
            self.parrent.ui.pushb_1_add.hide()

        if self.parrent.counter_of_elem_grid1 == 0:
            self.parrent.ui.pushb_1_add.show()

    def limit(self, button):
        if button.text() == 'Использовать предыдущее ограничение':
            self.ui.lineEdit_17.setDisabled(True)
            self.ui.lineEdit_17.clear()
            self.ui.pushButton_2.setDisabled(True)
        else:
            self.ui.lineEdit_17.setDisabled(False)
            self.ui.pushButton_2.setDisabled(False)






app = QApplication(sys.argv)
application = MainWin()
application.show()

sys.exit(app.exec())
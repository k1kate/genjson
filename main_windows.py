import json
import os
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import QtWidgets, QtGui, QtCore
from pydantic import BaseModel

from list_of_test import Ui_list_of_test
from test_form import Ui_Form
from chunk_form import Ui_Form3
from DispWin import DisplayWidget
from auth_win import Ui_auth_win
from genjson import Ui_Form2
from path import Ui_PathWin
from ent_win import Ui_login
from reg_win import Ui_login2


class WidTest(BaseModel):
    id: int
    is_main: bool
    num: object = None
    widget: object
    limit: list[str]
    necessary_test: list[int] = []
    test: list[str] = []

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
        self.ui.open_2.clicked.connect(self.create_win_edit)

    def create_win_path(self):
        self.close()
        self.w = PathWin()

        self.w.show()

    def create_win_edit(self):
        self.close()
        self.w = EditAddWin()

        self.w.show()


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
        self.w = AddWin(self)

        self.w.show()
        self.close()



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


class AddWin(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_list_of_test()
        self.ui.setupUi(self)
        self.parrent = parent
        self.counter = 0


        self.list_of_groups = []
        self.list_of_tests = [[]]
        self.counter_of_elem_grid1 = 0
        self.is_first_test = False
        self.group_num = 1
        self.name_files = []
        # self.path = self.parrent.path
        # self.namejson = self.parrent.namejson
        self.path = r'C:\Users\катя\Desktop\genjson2\тест'

        self.ui.label.setFixedSize(850, 67)
        self.layout_2 = QtWidgets.QVBoxLayout()

        self.pushb_2_add = QtWidgets.QPushButton('Добавить')
        self.pushb_2_add.setFixedSize(180, 36)
        self.pushb_2_create_file = QtWidgets.QPushButton('Создать файл')
        self.pushb_2_create_file.setFixedSize(180, 36)
        self.pushb_2_create_file.setStyleSheet("""QPushButton {
            background-color: #F0F0F0;
            border: 3px solid #B5B5B5; 
            border-radius: 10px; 
            padding: 3px;
            font: 12pt "Consolas" bold;
            }
            QPushButton:hover {
                background-color: #DADADA;
            }
            QPushButton:pressed {
                background-color: #919191;
            }""")
        self.pushb_2_add.setStyleSheet("""QPushButton {
            background-color: #F0F0F0;
            border: 3px solid #B5B5B5; 
            border-radius: 10px; 
            padding: 3px;
            font: 12pt "Consolas" bold;
            }
            QPushButton:hover {
                background-color: #DADADA;
            }
            QPushButton:pressed {
                background-color: #919191;
            }""")

        self.ui.pushb_1_add.clicked.connect(lambda: self.add_test(1))
        self.pushb_2_add.clicked.connect(lambda: self.add_test(2))
        self.pushb_2_create_file.clicked.connect(self.create_json_file)


    def add_test(self, btn): # окно со списками тестов
        self.w = FormWinChunk(btn, self)

        self.w.show()

    def create_json_file(self):
        self.json_file = {"setting_tests": []}

        for i in self.list_of_tests:
            limit = i.limit
            necessary_test = i.necessary_test
            test = i.test
            if i.is_main:
                type = "test"
            else:
                type = "main"

            self.json_file["setting_tests"].append({
                    "type_test": type,
                    "settings_test": {
                        "limitation_variable": limit,
                        "necessary_test": necessary_test,
                        "check_type": "one misstake"
                    },
                    "tests": []
            })

            for j in test:
                self.json_file["setting_tests"][-1]["tests"].append({
                    "score": int(j[3]),
                    "filling_type_variable": "{}.txt".format(j[0]),
                    "answer": "{}a.txt".format(j[0])
                })
            with open("{}\{}.json".format(self.path, self.namejson), "w") as write_file:
                json.dump(self.json_file, write_file)

        self.close()

    def closeEvent(self, event):
        msg = QMessageBox(self)
        msg.setWindowTitle("Внимание!")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Вы действительно хотите выйти?")

        buttonAceptar = msg.addButton("Да", QMessageBox.YesRole)
        buttonCancelar = msg.addButton("Нет", QMessageBox.RejectRole)
        msg.setDefaultButton(buttonCancelar)
        msg.exec_()

        if msg.clickedButton() == buttonAceptar:
            event.accept()
            self.w = MainWin()
            self.w.show()
        elif msg.clickedButton() == buttonCancelar:
            event.ignore()


class EditAddWin:
    def __init__(self, parent=None):
        super(AddWin, self).__init__()
        print('s')


class FormWinTest(QWidget):
    def __init__(self, wid=None, arr=None, row=None, parent: AddWin | None = None):
        super(FormWinTest, self).__init__()
        self.parrent = parent
        self.arr = arr
        self.wid = wid
        self.row = row
        self.fl = False #редактируется или нет

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.done)

        if self.arr != None and self.arr != False:
            self.edit()
            self.fl = True

    def done(self):
        self.name_file = self.ui.lineEdit_16.text()
        self.in_data = self.ui.plainTextEdit_7.toPlainText()
        self.out_data = self.ui.plainTextEdit_8.toPlainText()
        self.score = self.ui.lineEdit_19.text()
        fl = True

        if self.name_file != '' \
                and self.in_data != ''\
                and self.out_data != ''\
                and self.score.isdigit():
            if self.fl:
                self.clear_edit()

            for i in self.parrent.list_of_tests:
                for j in i.test:
                    if j[0] == self.name_file:
                        fl = False
            if fl:
                self.filling_test_table()
                self.record()
                self.create_test_file()
                self.close()
            elif fl == False:
                ErrorWin('Тест с таким именем уже существует')
        else:
            ErrorWin()

    def clear_edit(self):
        row = self.wid.tableWidget_2.currentRow()
        os.remove(r'{}\{}.txt'.format(self.parrent.path, self.arr[0]))
        os.remove(r'{}\{}a.txt'.format(self.parrent.path, self.arr[0]))
        for i in range(len(self.parrent.list_of_tests)):
            if self.wid == self.parrent.list_of_tests[i].widget:
                for j in self.parrent.list_of_tests[i].test:
                    if j == self.arr:
                        self.parrent.list_of_tests[i].test.remove(j)
                        break

    def create_test_file(self):
        f_in = open(r'{}\{}.txt'.format(self.parrent.path, self.name_file), 'w')
        f_out = open(r'{}\{}a.txt'.format(self.parrent.path, self.name_file), 'w')
        f_in.write(self.in_data)
        f_out.write(self.out_data)

    def filling_test_table(self):
        if self.fl:
            rowPosition = self.row
        else:
            rowPosition = self.wid.tableWidget_2.rowCount()
            self.wid.tableWidget_2.insertRow(rowPosition)

        self.wid.tableWidget_2.setItem(rowPosition, 0, QTableWidgetItem(self.name_file))
        self.wid.tableWidget_2.setItem(rowPosition, 1, QTableWidgetItem(self.in_data))
        self.wid.tableWidget_2.setItem(rowPosition, 2, QTableWidgetItem(self.out_data))
        self.wid.tableWidget_2.setItem(rowPosition, 3, QTableWidgetItem(self.score))

        self.wid.tableWidget_2.resizeRowsToContents()

    def record(self):
        fl = True
        for i in range(len(self.parrent.list_of_tests)):
            if self.wid == self.parrent.list_of_tests[i].widget:
                self.parrent.list_of_tests[i].test.append([self.name_file, self.in_data, self.out_data, self.score])
            if self.parrent.list_of_tests[i].test == []:
                fl = False
        if fl:
            self.parrent.pushb_2_create_file.setEnabled(True)

    def edit(self):
        self.ui.lineEdit_16.setText(self.arr[0])
        self.ui.plainTextEdit_7.appendPlainText(self.arr[1])
        self.ui.plainTextEdit_8.appendPlainText(self.arr[2])
        self.ui.lineEdit_19.setText(self.arr[3])


class FormWinChunk(QWidget):
    def __init__(self, btn, parent: AddWin | None = None):
        super(FormWinChunk, self).__init__()
        self.parrent = parent
        self.btn = btn
        self.list_cb_groups = []
        self.necesstest = []

        self.ui = Ui_Form3()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.done)
        self.ui.pushButton_2.clicked.connect(self.necessary_test_check)
        self.ui.lineEdit.textEdited.connect(self.color_necess)

        if self.parrent.counter_of_elem_grid1 == 0 or (self.parrent.counter == 1 and self.parrent.counter_of_elem_grid1 == 1):
            self.ui.pushButton_2.setEnabled(False)
            self.ui.lineEdit.setEnabled(False)

    def done(self):
        if self.necesstest != [0]:
            self.draw_wid()
            self.filling_chunk_table()
            self.call_win_test()
        elif self.necesstest == [0]:
            ErrorWin('Заполните правильно поле с необходимыми группами тестов')

    def color_necess(self, k):
        if k != '':
            self.ui.lineEdit.setStyleSheet("color: black;")
            self.necesstest = [0]

    def necessary_test_check(self):
        arr = []
        for i in self.parrent.list_of_tests[1:]:
            arr.append(i.id)

        necesstest = self.ui.lineEdit.text()

        try:
            if ',' in necesstest:
                necesstest = necesstest.replace(' ', '')
                necesstest = necesstest.split(',')
            elif ' ' in necesstest:
                necesstest = necesstest.strip()
                necesstest = necesstest.split(' ')
            necesstest = list(map(int, necesstest))
        except ValueError:
            self.ui.lineEdit.setStyleSheet("color: red;")
        else:
            for i in necesstest:
                if i in arr:
                    self.necesstest = necesstest
                    self.ui.lineEdit.setStyleSheet("color: green;")
                else:
                    self.ui.lineEdit.setStyleSheet("color: red;")
                    self.necesstest = [0]
                    break

    def call_win_test(self, arr=None, row=None):
        self.w = FormWinTest(self.wid, arr, row, parent=self.parrent)
        self.w.show()

    def filling_chunk_table(self):
        limit = self.ui.lineEdit_17.text()
        necces = self.ui.lineEdit.text()

        self.wid.tableWidget.setItem(0, 0, QTableWidgetItem(limit))
        self.wid.tableWidget.setItem(0, 1, QTableWidgetItem(necces))

    def draw_wid(self):
        self.wid = DisplayWidget()

        limit = [self.ui.lineEdit_17.text()]
        if ',' in limit[0]:
            limit = limit[0].split(',')
            limit = [i.lstrip() for i in limit]

        if self.btn == 1:
            self.adding_test_to_list(0)
        else:
            n = self.parrent.list_of_tests[-1].id + 1
            self.adding_test_to_list(n)

        self.parrent.counter += 1

        if self.parrent.counter == 1 and (not self.parrent.is_first_test):
            self.create_second_header()

        if self.btn == 2:
            n = self.parrent.list_of_tests[-1].id + 1
            self.obj = WidTest(id=n, is_main=False, num=self.lb_num, widget=self.wid, limit = limit, necessary_test=self.necesstest)
        else:
            self.obj = WidTest(id=0, is_main=True, widget=self.wid, limit=limit)

        if self.btn == 1:
            self.parrent.list_of_tests[0] = self.obj
        else:
            self.parrent.list_of_tests.append(self.obj)

        self.connectPB(self.obj)

        self.close()

    def connectPB(self, obj):
        self.wid.pb_del_chunk.clicked.connect(lambda state, x=obj: self.delete_wid(x))
        self.wid.pb_add_test.clicked.connect(self.call_win_test)
        self.wid.pb_del_test.clicked.connect(self.delete_test_table)
        self.wid.pb_edit_test.clicked.connect(self.edit_test_table)
        self.wid.pb_edit_chunk.clicked.connect(lambda state, x=obj: self.call_win_editchunk(x))

    def call_win_editchunk(self, obj):
        self.w = FormWinChunkEdit(self.btn, obj, self.parrent)

        self.w.show()

    def delete_test_table(self):
        row = self.wid.tableWidget_2.currentRow()
        if row > -1:
            a = [self.wid.tableWidget_2.item(row, 0).text(),
                 self.wid.tableWidget_2.item(row, 1).text(),
                 self.wid.tableWidget_2.item(row, 2).text(),
                 self.wid.tableWidget_2.item(row, 3).text()]
            self.wid.tableWidget_2.removeRow(row)
            self.wid.tableWidget_2.selectionModel().clearCurrentIndex()

            for i in range(len(self.parrent.list_of_tests)):
                if self.wid == self.parrent.list_of_tests[i].widget:
                    self.parrent.list_of_tests[i].test.remove(a)
                    if self.parrent.list_of_tests[i].test == []:
                        self.parrent.pushb_2_create_file.setEnabled(False)
                    break

            os.remove(r'{}\{}.txt'.format(self.parrent.path, a[0]))
            os.remove(r'{}\{}a.txt'.format(self.parrent.path, a[0]))

    def edit_test_table(self):
        row = self.wid.tableWidget_2.currentRow()
        if row > -1:
            arr = [self.wid.tableWidget_2.item(row, 0).text(),
                   self.wid.tableWidget_2.item(row, 1).text(),
                   self.wid.tableWidget_2.item(row, 2).text(),
                   self.wid.tableWidget_2.item(row, 3).text()]
            self.wid.tableWidget_2.selectionModel().clearCurrentIndex()

            self.call_win_test(arr, row)

    def create_second_header(self):
        self.main_head_lb = QLabel('Основные тесты:')
        self.main_head_lb.setFont(QtGui.QFont('Consolas', 25))
        self.main_head_lb.setFixedSize(400, 67)
        self.parrent.ui.verticalLayout_5.addWidget(self.main_head_lb)
        self.parrent.ui.verticalLayout_5.addLayout(self.parrent.layout_2)
        self.parrent.ui.verticalLayout_5.addWidget(self.parrent.pushb_2_add)
        self.parrent.ui.verticalLayout_5.addWidget(self.parrent.pushb_2_create_file, alignment=QtCore.Qt.AlignRight)

        self.parrent.ui.pushb_1_add.hide()

        self.parrent.is_first_test = True

    def delete_wid(self, obj):
        obj.widget.hide()
        self.parrent.ui.verticalLayout.setSpacing(0)

        if obj.is_main == False:
            obj.num.hide()

        if self.btn == 1:
            self.parrent.counter_of_elem_grid1 -= 1
            self.parrent.pushb_2_add.setEnabled(False)
            self.parrent.pushb_2_create_file.setEnabled(False)

        if self.parrent.counter_of_elem_grid1 == 0:
            self.parrent.list_of_tests[0] = []
        else:
            self.parrent.list_of_tests.remove(obj)

        if self.parrent.counter_of_elem_grid1 == 0:
            self.parrent.ui.pushb_1_add.show()

        self.parrent.counter -= 1

    def adding_test_to_list(self, n):
        if self.btn == 1:
            grid = self.parrent.ui.verticalLayout
            self.parrent.counter_of_elem_grid1 += 1
            self.parrent.pushb_2_add.setEnabled(True)
            self.parrent.pushb_2_create_file.setEnabled(True)
        else:
            grid = self.parrent.layout_2
            self.lb_num = QtWidgets.QLabel(' '+str(n)+':')
            self.lb_num.setFont(QtGui.QFont('Consolas', 16))
            self.lb_num.setStyleSheet('color: rgb(62, 81, 89);')
            grid.addWidget(self.lb_num)

        grid.addWidget(self.wid)

        if self.parrent.counter_of_elem_grid1 == 1:
            self.parrent.ui.pushb_1_add.hide()


class FormWinChunkEdit(FormWinChunk):
    def __init__(self, btn, obj, parent: AddWin | None = None):
        super().__init__(btn, parent)
        self.obj = obj

        self.ui.pushButton_2.clicked.connect(self.necessary_test_check)
        self.ui.lineEdit.textEdited.connect(self.color_necess)

        self.ui.lineEdit_17.setText(self.obj.widget.tableWidget.item(0, 0).text())

        if obj.id > 1:
            self.ui.lineEdit.setText(', '.join(list(map(str, self.obj.necessary_test))))
        if len(self.parrent.list_of_tests) > 1:
            if self.obj == self.parrent.list_of_tests[1]:
                self.ui.pushButton_2.setEnabled(False)
                self.ui.lineEdit.setEnabled(False)

    def done(self):
        self.obj.widget.tableWidget.setItem(0, 0, QTableWidgetItem(self.ui.lineEdit_17.text()))
        self.obj.widget.tableWidget.setItem(0, 1, QTableWidgetItem(self.ui.lineEdit.text()))

        self.create_json_file()

        if self.obj.id > 1 and self.necesstest == [0]:
            ErrorWin('Заполните правильно поле с необходимыми группами тестов')
        else:
            self.overwriting()

            self.close()

    def overwriting(self):
        for i in range(len(self.parrent.list_of_tests)):
            print(self.obj.id, self.parrent.list_of_tests[i].id)
            if self.parrent.list_of_tests[i].id == self.obj.id:
                self.parrent.list_of_tests[i].limit = self.ui.lineEdit_17.text()
                self.parrent.list_of_tests[i].necessary_test = self.necesstest

    def color_necess(self, k):
        if k != '':
            self.ui.lineEdit.setStyleSheet("color: black;")
            self.necesstest = [0]

    def necessary_test_check(self):
        arr = []
        for i in self.parrent.list_of_tests[1:]:
            if self.obj.id != i.id:
                arr.append(i.id)

        try:
            necesstest = self.ui.lineEdit.text()
            if ',' in necesstest:
                necesstest = necesstest.replace(' ', '')
                necesstest = necesstest.split(',')
            elif ' ' in necesstest:
                necesstest = necesstest.strip()
                necesstest = necesstest.split(' ')
            necesstest = list(map(int, necesstest))
        except ValueError:
            self.ui.lineEdit.setStyleSheet("color: red;")
        else:
            for i in necesstest:
                if i in arr:
                    self.necesstest = necesstest
                    self.ui.lineEdit.setStyleSheet("color: green;")
                else:
                    self.ui.lineEdit.setStyleSheet("color: red;")
                    break

app = QApplication(sys.argv)
# application = Auth()
application = MainWin()
application.show()

sys.exit(app.exec())




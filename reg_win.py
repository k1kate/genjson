# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login2(object):
    def setupUi(self, login2):
        login2.setObjectName("login2")
        login2.resize(1025, 747)
        login2.setMinimumSize(QtCore.QSize(1025, 747))
        login2.setMaximumSize(QtCore.QSize(1025, 747))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        login2.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(login2)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 150, 861, 530))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(32)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(100, 15, 105, -1)
        self.gridLayout.setHorizontalSpacing(31)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.le_password = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.le_password.setFont(font)
        self.le_password.setObjectName("le_password")
        self.gridLayout.addWidget(self.le_password, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setStatusTip("")
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.le_name = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.le_name.setFont(font)
        self.le_name.setObjectName("le_name")
        self.gridLayout.addWidget(self.le_name, 1, 1, 1, 1)
        self.le_password2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.le_password2.setFont(font)
        self.le_password2.setObjectName("le_password2")
        self.gridLayout.addWidget(self.le_password2, 5, 1, 1, 1)
        self.le_name3 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.le_name3.setFont(font)
        self.le_name3.setObjectName("le_name3")
        self.gridLayout.addWidget(self.le_name3, 3, 1, 1, 1)
        self.le_name2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.le_name2.setFont(font)
        self.le_name2.setObjectName("le_name2")
        self.gridLayout.addWidget(self.le_name2, 2, 1, 1, 1)
        self.le_login = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.le_login.setFont(font)
        self.le_login.setObjectName("le_login")
        self.gridLayout.addWidget(self.le_login, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.pb_done = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_done.sizePolicy().hasHeightForWidth())
        self.pb_done.setSizePolicy(sizePolicy)
        self.pb_done.setMinimumSize(QtCore.QSize(182, 0))
        self.pb_done.setMaximumSize(QtCore.QSize(200, 40))
        self.pb_done.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pb_done.setFont(font)
        self.pb_done.setStyleSheet("QPushButton {\n"
"        background-color: #F0F0F0;\n"
"        border: 3px solid #B5B5B5; \n"
"        border-radius: 10px; \n"
"        padding: 6px;\n"
"        font: 16pt \"Consolas\";\n"
"    \n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #DADADA;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #919191;\n"
"    }")
        self.pb_done.setObjectName("pb_done")
        self.verticalLayout.addWidget(self.pb_done, 0, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(login2)
        self.label_7.setGeometry(QtCore.QRect(400, 50, 253, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pb_home = QtWidgets.QPushButton(login2)
        self.pb_home.setGeometry(QtCore.QRect(30, 30, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_home.sizePolicy().hasHeightForWidth())
        self.pb_home.setSizePolicy(sizePolicy)
        self.pb_home.setMinimumSize(QtCore.QSize(70, 70))
        self.pb_home.setMaximumSize(QtCore.QSize(70, 70))
        self.pb_home.setStyleSheet("QPushButton {\n"
"        background-color: #F0F0F0;\n"
"        border: 3px solid #B5B5B5; \n"
"        border-radius: 10px; \n"
"        padding: 6px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #DADADA;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #919191;\n"
"    }")
        self.pb_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/house-black-silhouette-without-door.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_home.setIcon(icon)
        self.pb_home.setIconSize(QtCore.QSize(40, 40))
        self.pb_home.setObjectName("pb_home")

        self.retranslateUi(login2)
        QtCore.QMetaObject.connectSlotsByName(login2)

    def retranslateUi(self, login2):
        _translate = QtCore.QCoreApplication.translate
        login2.setWindowTitle(_translate("login2", "Form"))
        self.label_3.setText(_translate("login2", "Отчество"))
        self.label_4.setText(_translate("login2", "Имя"))
        self.label_2.setText(_translate("login2", "Пароль"))
        self.label_5.setText(_translate("login2", "Фамилия"))
        self.label.setText(_translate("login2", "Логин"))
        self.label_6.setText(_translate("login2", "Повторение пароля"))
        self.pb_done.setText(_translate("login2", "Готово"))
        self.label_7.setText(_translate("login2", "Регистрация"))

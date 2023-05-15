# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_auth_win(object):
    def setupUi(self, auth_win):
        auth_win.setObjectName("auth_win")
        auth_win.resize(1025, 747)
        auth_win.setMinimumSize(QtCore.QSize(1025, 747))
        auth_win.setMaximumSize(QtCore.QSize(1025, 747))
        self.layoutWidget = QtWidgets.QWidget(auth_win)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 1021, 741))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(50, 0, 50, 0)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.auth = QtWidgets.QPushButton(self.layoutWidget)
        self.auth.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auth.sizePolicy().hasHeightForWidth())
        self.auth.setSizePolicy(sizePolicy)
        self.auth.setMaximumSize(QtCore.QSize(500, 80))
        self.auth.setSizeIncrement(QtCore.QSize(0, 0))
        self.auth.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas 12")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.auth.setFont(font)
        self.auth.setTabletTracking(False)
        self.auth.setAcceptDrops(False)
        self.auth.setToolTip("")
        self.auth.setToolTipDuration(-1)
        self.auth.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.auth.setAutoFillBackground(False)
        self.auth.setStyleSheet("QPushButton {\n"
"        background-color: #F0F0F0;\n"
"        border: 5px solid #B5B5B5; \n"
"        border-radius: 10px; \n"
"        padding: 6px;\n"
"        font: 28pt \"Consolas\" bold;\n"
"    \n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #DADADA;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #919191;\n"
"    }")
        self.auth.setCheckable(False)
        self.auth.setObjectName("auth")
        self.horizontalLayout_2.addWidget(self.auth)
        self.reg = QtWidgets.QPushButton(self.layoutWidget)
        self.reg.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reg.sizePolicy().hasHeightForWidth())
        self.reg.setSizePolicy(sizePolicy)
        self.reg.setMaximumSize(QtCore.QSize(500, 80))
        self.reg.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas 12")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.reg.setFont(font)
        self.reg.setTabletTracking(False)
        self.reg.setAcceptDrops(False)
        self.reg.setToolTipDuration(-1)
        self.reg.setAutoFillBackground(False)
        self.reg.setStyleSheet("QPushButton {\n"
"        background-color: #F0F0F0;\n"
"        border: 5px solid #B5B5B5; \n"
"        border-radius: 10px; \n"
"        padding: 6px;\n"
"        font: 28pt \"Consolas\" bold;\n"
"    \n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #DADADA;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #919191;\n"
"    }")
        self.reg.setObjectName("reg")
        self.horizontalLayout_2.addWidget(self.reg)

        self.retranslateUi(auth_win)
        QtCore.QMetaObject.connectSlotsByName(auth_win)

    def retranslateUi(self, auth_win):
        _translate = QtCore.QCoreApplication.translate
        auth_win.setWindowTitle(_translate("auth_win", "Form"))
        self.auth.setText(_translate("auth_win", "Войти"))
        self.reg.setText(_translate("auth_win", "Регистрация"))
